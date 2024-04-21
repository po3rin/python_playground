import json
import os

import gokart
import luigi
import pandas as pd
import vertexai
from vertexai.language_models import TextGenerationModel

project = os.getenv("GOOGLE_CLOUD_PROJECT_ID")
location = os.getenv("GOOGLE_CLOUD_LOCATION")


class SearchQueries(gokart.TaskOnKart):
    """
    与えられたクエリに関連する記事タイトルと関連のない記事タイトルを生成するタスク
    """

    size: int = luigi.IntParameter(default=10)
    chunk: int = luigi.IntParameter(default=10)

    def run(self):
        vertexai.init(project=project, location=location)
        parameters = {
            "temperature": 0.5,  # Temperature controls the degree of randomness in token selection.
            "max_output_tokens": 1000,
            "top_p": 0.8,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
            "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
        }

        model = TextGenerationModel.from_pretrained("text-bison@002")

        results = []
        for i in range(int(self.size / self.chunk)+1):
            response = model.predict(
                f"""
                医療系の検索クエリを{self.chunk}個作成してください。
                結果は、以下のようなJSON形式で提出してください。

                [{{"query": "クエリの内容1"}},{{"query": "クエリの内容2"}}]
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
                print(json_str)
                raise e
            results.extend(result)

        df = pd.DataFrame(results)
        self.dump(df)


def main():
    df = gokart.build(SearchQueries(size=200))
    df.to_csv("data/generated_queries.csv", index=False)


if __name__ == "__main__":
    main()
