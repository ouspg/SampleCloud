from flask import Flask
from flask_restful import Resource

class Find(Resource):

    def get(self, metadata):
        return "This funtion will return info for sample arhives that match the search pattern."

class Info(Resource):

    def get(self, id):
        return "This function shows metadata for the queried sample ID."

class Download(Resource):

    def get(self, id):
        return "This function will return a requested sample ID archive file."

class Upload(Resource):

    def post(self, metadata):
        return "This function will upload an sample archive file and applies provided metadata to it."

class Edit(Resource):
