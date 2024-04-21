import os

import gokart

from tasks.llm.vertex import GenerateTestCollectionWithVertexAI
from tasks.queries import LoadQueries
from tasks.upload.gcs import UploadGCS

project = os.getenv("GOOGLE_CLOUD_PROJECT_ID")
location = os.getenv("GOOGLE_CLOUD_LOCATION")


def main():
    bucket_name = "llm-testcollection"

    queries = LoadQueries(csv_file_path="data/queries.csv")
    upload = UploadGCS(
        queries=queries, bucket_name=bucket_name, destination_blob_name="prompts.jsonl"
    )
    generate_search_dataset_task = GenerateTestCollectionWithVertexAI(
        project=project,
        location=location,
        destination_uri_prefix=f"gs://{bucket_name}/result",
        source_blob_url=upload,
    )
    gokart.build(generate_search_dataset_task)


if __name__ == "__main__":
    main()
