from flask import Flask
from flask_restful import Resource

import package_about, system_about

MODULES = {
    "package": package_about.about,
    "system": system_about.about
}

class Viewer(Resource):

    def get(self, module = None, category = None, value = None):

        if module:
            data = MODULES[module]

            if category:
                data = data[category]

                if value:
                    data = data[value]

        else:
            data = list(MODULES.keys())

        return data
