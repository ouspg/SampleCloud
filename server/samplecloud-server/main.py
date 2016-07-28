#!/usr/bin/env python3

from flask import Flask
from flask_restful import Api

import about
import samples

app = Flask("samplecloud-server")
api = Api(app)

# About API components
api.add_resource(about.Category, "/about/<category>")
api.add_resource(about.SubCategory, "/about/<category>/<subcategory>")
api.add_resource(about.SubCategoryValue, "/about/<category>/<subcategory>/<value>")

# Samples API components
api.add_resource(samples.Find, "/samples/find")
api.add_resource(samples.Info, "/samples/info")
api.add_resource(samples.Download, "/samples/download")
api.add_resource(samples.Upload, "/samples/upload")