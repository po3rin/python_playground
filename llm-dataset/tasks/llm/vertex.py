import gokart
import luigi
import vertexai
from vertexai.language_models import TextGenerationModel


class GenerateTestCollectionWithVertexAI(gokart.TaskOnKart):
    """
    テストコレクションの作成
    """

    project: str = luigi.Parameter()
    location: str = luigi.Parameter()
    destination_uri_prefix: str = luigi.Parameter()
    source_blob_url: str = gokart.TaskInstanceParameter()

    def run(self):
        source_blob_url = self.load("source_blob_url")
        vertexai.init(project=self.project, location=self.location)
        parameters = {
            "temperature": 1,
            "max_output_tokens": 1000,
            "top_p": 0.95,
            "top_k": 40,
        }
        model = TextGenerationModel.from_pretrained("text-bison")

        batch_prediction_job = model.batch_predict(
            dataset=source_blob_url,
            destination_uri_prefix=self.destination_uri_prefix,
            model_parameters=parameters,
        )

        batch_prediction_job.wait_for_resource_creation()
        self.dump("done")
