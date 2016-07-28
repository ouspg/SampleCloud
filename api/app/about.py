from flask_restful import Resource

class All(Resource):

    VALUES = {
        "version": __version__,
        "maintainer": __maintainer__
    }

    def get(self):
            return VALUES

class Version(Resource):

    def get(self, humanr):
        if humanr == True:
            return "Api version: " + __version__
        elif humanr == False:
            return __version__

class Maintainer(Resource):

    def get(self, humanr):
        if humanr == True:
            return "Project maintainer: " + __maintainer__
        elif humanr == False:
            return __maintainer__
