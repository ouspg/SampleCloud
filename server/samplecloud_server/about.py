from flask import Flask
from flask_restful import Resource

import package_about, system_about

modules = {
    "package": package_about.about,
    "system": system_about.about
}

class CategoryView(Resource):

    def get(self, module, category):

        return modules[module][category]

class ValueView(Resource):

    def get(self, module, category, value):

        return modules[module][category][value]
