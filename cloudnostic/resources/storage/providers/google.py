import io
import os

from google.cloud.storage import Client

GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", None)


def set_credentials(credentials):
    global GOOGLE_APPLICATION_CREDENTIALS
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials


class GoogleBucket:
    def __init__(self, storage_name):
        self.credentials = GOOGLE_APPLICATION_CREDENTIALS
        self.client = self.create_client(storage_name)

    def download_blob_bytes(self, blob_name):
        blob = self.client.blob(blob_name)
        return io.BytesIO(blob.download_as_bytes())

    def upload_blob_bytes(self, blob_name, data):
        self.client.blob(blob_name).upload_from_file(data)

    def create_client(self, storage_name):
        return Client().bucket(storage_name)
