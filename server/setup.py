from setuptools import setup
from .samplecloud-server import app_info

setup(
    name = "samplecloud-api-server",
    version = app_info.release_info["release_version"],
    author = app_info.maintainer_info["maintainer_name"],
    description = app_info.project_info["project_description"],
    license = "MIT",
    url = "https://github.com/ouspg/SampleCloud",
    packages=['samplecloud-api', 'tests'],
)
