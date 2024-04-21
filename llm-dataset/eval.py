import random
from statistics import mean

import numpy as np
import pandas as pd
from elasticsearch import Elasticsearch
from tqdm import tqdm


def dcg(gain, k=None):
    """calc dcg value"""
    if k is None:
        k = gain.shape[0]

    ret = gain[0]
    for i in range(1, k):
        ret += gain[i] / np.log2(i + 1)
    return ret


def ndcg(y, k=None, powered=False) -> float:
    """calc nDCG value"""

    dcg_score = dcg(y, k=k)

    ideal_sorted_scores = np.sort(y)[::-1]
    ideal_dcg_score = dcg(ideal_sorted_scores, k=k)

    return dcg_score / ideal_dcg_score


def main():
    client = Elasticsearch(hosts=["http://localhost:9200"])
    if not client.ping():
        raise Exception("Elasticsearch is not running.")

    df = pd.read_csv("data/dataset.csv")
    docs = df.to_dict(orient="records")
    queries = df["query"].drop_duplicates().tolist()
    random.shuffle(docs)

    for d in docs:
      client.index(index='docs', body=d, pipeline='japanese-text-embeddings')

    results_a = []
    results_b = []
    for q in tqdm(queries):
        result_a = client.search(
            index="docs",
            body={
                "_source": {"includes": ["title", "body", "score", "reason"]},
                "query": {
                    "bool": {
                        "should": {"match": {"title": q}},
                        "filter": {"match": {"query": q}},
                    }
                },
            },
        )
        scores_a = [r["_source"]["score"] for r in result_a["hits"]["hits"]]

        result_b = client.search(
            index="docs",
            body={
                "_source": {"includes": ["title", "body", "score", "reason"]},
                "query": {
                    "bool": {
                        "should": {"match": {"title": q}},
                        "filter": {"match": {"query": q}},
                    }
                },
                "knn": {
                    "field": "text_embedding.predicted_value",
                    "k": 10,
                    "num_candidates": 50,
                    "query_vector_builder": {
                        "text_embedding": {
                            "model_id": "cl-tohoku__bert-base-japanese-v2",
                            "model_text": q,
                        }
                    },
                    "filter": {"bool": {"filter": {"match": {"query": q}}}},
                },
            },
        )

        scores_a = [r["_source"]["score"] for r in result_a["hits"]["hits"]]
        scores_b = [r["_source"]["score"] for r in result_b["hits"]["hits"]]
        # print("===========================")
        # print(f"query: {q}")
        # print("---------scores------------")
        # print(scores_a)
        # print(scores_b)
        # print("---------------------------")
        if len(scores_a) == 0 or len(scores_b) == 0:
            continue

        results_a.append(ndcg(np.array(scores_a)))
        results_b.append(ndcg(np.array(scores_b)))

    # print(results_a)
    # print(results_b)

    print(mean(results_a))
    print(mean(results_b))


if __name__ == "__main__":
    main()
