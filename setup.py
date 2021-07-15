from setuptools import find_packages, setup

setup(
    name="cloudnostic-resources-storage",
    description="Abstract class",
    author="Some Guy",
    version="0.0.1",
    packages=find_packages(),
    namespace_packages=["cloudnostic", "cloudnostic.resources"],
    install_requires=[
        "google-cloud-storage",
        "azure-storage-blob",
    ],
)
