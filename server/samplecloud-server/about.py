from flask import Flask
from flask_restful import Resource

from __init__ import __version__

class Version(Resource):

    def get(self):
        return __version__

class Project(Resource):

    def get(self):

        project_description = "SampleCloud is an api centric web application for sharing \
                                sample arhive files for software fuzzing purposes."
        return project_description

class Author(Resource):

    def get(self):

        author_info = {
            name: "Pauli Huttunen",
            nick: "WhiteEyeDoll"
        }

        return author_info
