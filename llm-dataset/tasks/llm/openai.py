import gokart
import luigi
from openai import OpenAI


class GenerateTestCollectionWithOpenAI(gokart.TaskOnKart):
    """
    与えられたクエリに関連する記事タイトルと関連のない記事タイトルを生成するタスク
    """

    input_file_id: int = gokart.TaskInstanceParameter()

    def run(self):
        client = OpenAI()
        input_file_id = self.load("input_file_id")
        results = []
        batch = client.batches.create(
            completion_window="24h",
            endpoint="/v1/chat/completions",
            input_file_id=input_file_id,
        )

        with client.batches.with_streaming_response.retrieve(
            batch.id,
        ) as response:
            batch = response.parse()
            print(batch)
            self.dump(batch)
