#!/usr/bin/env python3

from flask import Flask
from flask_restful import Api

import about

app = Flask("samplecloud-api")
api = Api(app)

api.add_resource(about.All, "/about")
api.add_resource(about.Version, "/about/version")
api.add_resource(about.Maintainer, "/about/maintainer")
