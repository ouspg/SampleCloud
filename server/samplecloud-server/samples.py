from flask import Flask
from flask_restful import Resource

class Find(Resource):

    def get(self):
        return "This api will return info for sample arhives that match the search pattern."

class Info(Resource):

    def get(self):
        return "This api shows metadata for the give sample ID."

class Download(Resource):

    def get(self):
        return "This api will return a sample archive file for the given ID."

class Upload(Resource):

    def get(self):
        return "This api will upload an sample archive file and applies provided metadata to it."

class Edit(Resource):

    def get(self):
        return "This api will be used to edit sample archive file metadata."
