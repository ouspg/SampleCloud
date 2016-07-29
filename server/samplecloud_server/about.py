from flask import Flask
from flask_restful import Resource

import package

categories = {
    "package": package.pkg
}

class Category(Resource):

    def get(self, category):
        return categories[category]

class SubCategory(Resource):

    def get(self, category, subcategory):
        return categories[category][subcategory]

class SubCategoryValue(Resource):

    def get(self, category, subcategory, value):
        return categories[category][subcategory][value]
