from flask import Flask
from flask_restful import Resource

class Create(Resource):
    """Create a user"""

    def post(self, username, realname, email, password):
        return

class Delete(Resource):
    """Delete a user"""

    def delete(self, username, password):
        return

class Query(Resource):
    """Show users information"""

    def get(self, username):
        return

class Password(Resource):
    """Change users password"""

    def put(self, username, old_password, new_password):
        return

class Edit(Resource):
    """Edit users information"""

    def put(self, realname = None, email = None):
        return
