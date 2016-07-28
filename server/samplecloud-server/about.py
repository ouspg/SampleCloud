from flask import Flask
from flask_restful import Resource

import project

class Project(Resource):

    def get(self):
        return project.info

class Version(Resource):

    def get(self):
        return project.release

class Maintainer(Resource):

    def get(self):
        return project.maintainer
