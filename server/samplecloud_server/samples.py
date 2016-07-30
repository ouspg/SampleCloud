from flask import Flask
from flask_restful import Resource

class Search(Resource):
    """Search for samples that match given parameters"""

    def get(self):
        return

class Show(Resource):
    """Show metadata information of a sample by id"""

    def get(self, sample_id):
        return

class Upload(Resource):
    """Upload a sample and apply give metadata to it"""

    def post(self):
        return

class Download(Resource):
    """Download a sample archive file by id"""

    def get(self, sample_id):
        return

class Edit(Resource):
    """Edit a sample metadata by id"""

    def put(self):
        return

class Delete(Resource):
    """Delete a sample by id"""

    def delete(self, sample_id):
        return
