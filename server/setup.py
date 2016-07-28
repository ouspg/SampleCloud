from setuptools import setup
from .samplecloud-api import __version__

setup(
    name = "samplecloud-api-server",
    version = __version__,
    author = "Pauli Huttunen",
    description = ("SampleCloud api component for client usage."),
    license = "MIT",
    url = "https://github.com/ouspg/SampleCloud",
    packages=['samplecloud-api', 'tests'],
)
