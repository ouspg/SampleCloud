from flask import Flask
from flask_restful import Resource

class Create(Resource):

    def get(self):
        return "This api will be used for user creation."

class Delete(Resource):

    def get(self):
        return "This api will be used for user deletion."

class Query(Resource):

    def get(self):
        return "This api will be used to query user information."

class UpdatePassword(Resource):

    def get(self):
        return "This api will be used to change user password"

class Status(Resource):

    def get(self):
        return "This function will be used to activate, freeze, and ban users."
