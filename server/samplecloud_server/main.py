#!/usr/bin/env python3

from flask import Flask
from flask_restful import Api

import about

app = Flask("samplecloud_server")
api = Api(app)

# About API components
api.add_resource(about.Viewer, "/about",
                                "/about/<module>",
                                "/about/<module>/<category>",
                                "/about/<module>/<category>/<value>")
