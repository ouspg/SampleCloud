#!/usr/bin/env python3

from flask import Flask
from flask_restful import Api

import about
import samples

app = Flask("samplecloud-server")
api = Api(app)

# About API components
api.add_resource(about.CategoryView, "/about/<category>")
api.add_resource(about.ValueView, "/about/<category>/<value>")

# Samples API components
api.add_resource(samples.Find, "/data/samples/find")
api.add_resource(samples.Info, "/data/samples/info")
api.add_resource(samples.Download, "/data/samples/download")
api.add_resource(samples.Upload, "/data/samples/upload")
