from flask import Flask
from flask_restful import Resource

from __init__ import __version__

class Version(Resource):

    def get(self):
        return __version__
