from flask import Flask
from flask_restful import Resource

class Create(Resource):

    def post(self, username, passwd):
        return "This fuction will be used for user creation."

class Delete(Resource):

    def delete(self, username):
        return "This function will be used for user deletion."

class Modify(Resource):

class Activate(Resource):

class Deactivate(Resource):
