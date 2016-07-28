#!/usr/bin/env python3

from flask import Flask
from flask_restful import Api

import about

app = Flask("samplecloud-server")
api = Api(app)

api.add_resource(about.Version, "/about/version")
