import json
import random

import luigi
import gokart
import pandas as pd
from openai import OpenAI


def load_queries():
  with open('data/queries.csv', 'r') as f:
    return [line for line in f.readlines()]


class SearchDataset(gokart.TaskOnKart):
  """
  与えられたクエリに関連する記事タイトルと関連のない記事タイトルを生成するタスク
  """

  size: int = luigi.IntParameter(default=200)

  def run(self):
    client = OpenAI()

    queries = load_queries()
    queries = random.sample(queries, self.size)

    results = []
    for q in queries:
      completion = client.chat.completions.create(
        model='gpt-4-1106-preview',
        messages=[
          {
              'role': 'system',
              'content': f'''
              「{q}」という医療系の検索クエリに関係のある記事タイトルと関係のない記事タイトルを複数作成し、クエリとの関連度を0~2の3段階で付与してください。2が最も関連度が高いものとします。
              関連度0はクエリと全く関係のないタイトル、関連度1は直接の関連はないが部分的、または間接的に関係のあるタイトル、関連度2はクエリと直接関係のあるタイトルとします。
              結果は、以下のようなJSON形式で提出してください。

              {{"query": "クエリの内容", "title": "クエリと関連のある記事タイトル", "score": 2, "reason": "理由"}}
              '''
          }
        ]
      )

      md_str = completion.choices[0].message.content
      json_str = md_str.removeprefix('```json').removesuffix('```').replace('\n', '').replace(' ', '')
      result = json.loads(json_str)
      results.extend(result)

    df = pd.DataFrame(results)
    self.dump(df)


def main():
  df = gokart.build(SearchDataset(size=10))
  df.to_csv('data/dataset.csv', index=False)


if __name__ == '__main__':
  main()