import os
import json
import random

import luigi
import gokart
import pandas as pd
from tqdm import tqdm
import vertexai
from vertexai.language_models import TextGenerationModel


project = os.getenv("GOOGLE_CLOUD_PROJECT_ID")
location = os.getenv("GOOGLE_CLOUD_LOCATION")


def load_queries():
    with open("data/queries.csv", "r") as f:
        return [line for line in f.readlines()]


class SearchDataset(gokart.TaskOnKart):
    """
    与えられたクエリに関連する記事タイトルと関連のない記事タイトルを生成するタスク
    """

    size: int = luigi.IntParameter(default=10)

    def run(self):
        vertexai.init(project=project, location=location)
        parameters = {
            "temperature": 1,
            "max_output_tokens": 1000,
            "top_p": 0.8,
            "top_k": 40,
        }

        model = TextGenerationModel.from_pretrained("text-bison@002")

        queries = load_queries()
        queries = random.sample(queries, self.size)

        results = []
        errors = []
        for q in tqdm(queries):
            response = model.predict(
                f"""
              「{q}」という医療系の検索クエリに関係のある記事タイトルと関係のない記事タイトルを複数作成し、クエリとの関連度を0~2の3段階で付与してください。2が最も関連度が高いものとします。
              関連度0はクエリと全く関係のないタイトル、関連度1は直接の関連はないが部分的、または間接的に関係のあるタイトル、関連度2はクエリと直接関係のあるタイトルとします。最大で8個作成してください。関連度は0,1,2全てのパターンが必ず出現するようにしてください。
              結果は、以下のようなJSON形式で提出してください。
              [{{"query": "クエリの内容", "title": "クエリと関連のある記事タイトル", "score": 2, "reason": "理由"}},{{"query": "クエリの内容", "title": "クエリと関連のある記事タイトル", "score": 2, "reason": "理由"}}]
                """,
                **parameters,
            )

            json_str = (
                response.text.removeprefix(" ")
                .removeprefix("```json")
                .removeprefix("```JSON")
                .removesuffix("```")
                .replace("\n", "")
                .replace(" ", "")
            )
            try:
                result = json.loads(json_str)
            except Exception as e:
                errors.append(json_str)
                continue
            results.extend(result)

        df = pd.DataFrame(results)
        print(f'{len(errors)} errors')
        self.dump(df)


def main():
    df = gokart.build(SearchDataset(size=200))
    df.to_csv("data/dataset.csv", index=False)


if __name__ == "__main__":
    main()
