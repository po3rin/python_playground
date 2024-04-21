import io
import json
import os
import random

import gokart
import luigi
import pandas as pd
import vertexai
from google.cloud import storage
from tqdm import tqdm
from vertexai.language_models import TextGenerationModel

project = os.getenv("GOOGLE_CLOUD_PROJECT_ID")
location = os.getenv("GOOGLE_CLOUD_LOCATION")


def load_queries():
    with open("data/queries.csv", "r") as f:
        return [line for line in f.readlines()]


class UploadPromptsBatch(gokart.TaskOnKart):
    """
    batchで投げるためのpromptを作成する
    """

    size: int = luigi.IntParameter(default=10)
    bucket_name: str = luigi.Parameter()
    destination_blob_name: str = luigi.Parameter()

    def run(self):
        queries = load_queries()
        queries = random.sample(queries, self.size)

        s = io.StringIO()
        for q in tqdm(queries):
            prompt = f'''
                「{q}」という医療系の検索クエリに関係のある記事タイトルと関係のない記事タイトルを複数作成し、クエリとの関連度を0~2の3段階で付与してください。2が最も関連度が高いものとします。
                関連度0はクエリと全く関係のないタイトル、関連度1は直接の関連はないが部分的、または間接的に関係のあるタイトル、関連度2はクエリと直接関係のあるタイトルとします。最大で8個作成してください。関連度は0,1,2全てのパターンが必ず出現するようにしてください。
                結果は、以下のようなkeyを持つJSON形式で提出してください。
                query: クエリの内容
                title: クエリと関連のある記事タイトル
                score: 関連度(0~2)
                reason": "scoreの理由
            '''

            s.write('{"prompt":"' + prompt + '"}')
            s.write('\n')

        value = s.getvalue()
        print(value)
        storage_client = storage.Client()
        bucket = storage_client.bucket(self.bucket_name)
        blob = bucket.blob(self.destination_blob_name)
        blob.upload_from_string(value)
        s.close()

        self.dump(f'gs://{self.bucket_name}/{self.destination_blob_name}')


class GenerateTestCollection(gokart.TaskOnKart):
    """
    テストコレクションの作成
    """

    bucket_name: str = luigi.Parameter()
    destination_blob_name: str = luigi.Parameter()
    source_blob_url: str = gokart.TaskInstanceParameter()
    
    def run(self):
        source_blob_url = self.load('source_blob_url')
        vertexai.init(project=project, location=location)
        parameters = {
            "temperature": 1,
            "max_output_tokens": 1000,
            "top_p": 0.95,
            "top_k": 40,
        }
        model = TextGenerationModel.from_pretrained("text-bison@002")

        batch_prediction_job = model.batch_predict(
            job_display_name='search-dataset-batch',
            machine_type='n1-standard-4',
            gcs_source=[source_blob_url],
            gcs_destination_prefix=f'gs://{self.bucket_name}/{self.destination_blob_name}'
        )

        batch_prediction_job.wait_for_resource_creation()
        self.dump('done')


def main():
    bucket_name='llmtestcollection',
    upload_task = UploadPromptsBatch(
        size=200,
        bucket_name=bucket_name,
        destination_blob_name='prompts.jsonl'
    )
    generate_search_dataset_task = GenerateTestCollection(
        bucket_name=bucket_name,
        destination_blob_name='test_collection.jsonl',
        source_blob_url=upload_task,
    )
    gokart.build(generate_search_dataset_task)


if __name__ == "__main__":
    main()
