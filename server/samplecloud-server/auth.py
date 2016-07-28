from flask import Flask
from flask_restful import Resource

class Normal(Resource):

class Token(Resource):

    def get(self, token):
        return "This function will authenticate an user with a token."
