from setuptools import setup
from samplecloudwebapi import package_about

setup(
    name = "samplecloudwebapi",
    version = package_about.about["release"]["version"],
    author = package_about.about["author"]["name"],
    description = package_about.about["info"]["description"],
    license = "MIT",
    url = "https://github.com/ouspg/SampleCloud",
    packages=["samplecloudwebapi", "tests"],
)

