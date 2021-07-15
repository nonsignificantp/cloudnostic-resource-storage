import io
import os

from azure.storage.blob import ContainerClient

AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING", None)


def set_credentials(credentials):
    global AZURE_STORAGE_CONNECTION_STRING
    AZURE_STORAGE_CONNECTION_STRING = credentials


class AzureContainer:
    """"""

    def __init__(self, storage_name):
        self.credentials = AZURE_STORAGE_CONNECTION_STRING
        self.client = self.create_client(storage_name)

    def download_blob_bytes(self, blob_name):
        blob = self.client.download_blob(blob_name)
        return io.BytesIO(blob.content_as_bytes())

    def upload_blob_bytes(self, blob_name, data):
        self.client.upload_blob(blob_name, data)

    def create_client(self, storage_name):
        return ContainerClient.from_connection_string(self.credentials, storage_name)
