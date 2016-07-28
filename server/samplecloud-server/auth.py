from flask import Flask
from flask_restful import Resource

class Normal(Resource):

    def get(self):
        return "This api will authenticate users with a username/password combination."

class Token(Resource):

    def get(self):
        return "This api will authenticate users with a token."
