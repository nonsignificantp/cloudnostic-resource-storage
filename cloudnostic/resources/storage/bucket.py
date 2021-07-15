import re

from cloudnostic.resources.storage import _errors
from cloudnostic.resources.storage.providers import azure, google

# Regex pattern for bucket urls validation
BUCKET_VALID_URL = r"(aws|gc|s3|wasb)://[\w\-\_]+$"


class Bucket:
    """"""

    def __init__(self, url: str):
        self.entity = self._entity_from_url(url)

    def get(self, blob_name: str) -> bytes:
        """"""
        return self.entity.download_blob_bytes(blob_name)

    def put(self, blob_name: str, data: bytes) -> None:
        """"""
        self.entity.upload_blob_bytes(blob_name, data)

    def _entity_from_url(self, url: str):
        """"""
        if not self._valid_url(url):
            raise _errors.INVALID_URL

        cloud, storage_name = url.split("://")

        if cloud in ["wasb"]:
            return azure.AzureContainer(storage_name)

        if cloud in ["gc"]:
            return google.GoogleBucket(storage_name)

        if cloud in ["s3", "aws"]:
            return NotImplemented

    def _valid_url(self, url: str):
        """"""
        if re.match(BUCKET_VALID_URL, url):
            return True
        return False


def create_buckets(*urls):
    """"""
    if len(urls) == 1:
        return Bucket(urls[0])
        
    for url in urls:
        yield Bucket(url)
