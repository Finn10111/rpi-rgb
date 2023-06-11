#!/usr/bin/python
import os
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, os.path.dirname(__file__))
activate_this = os.path.join(os.path.dirname(__file__), 'bin/activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from app import create_app


def application(environ, start_response):
    ENVIRONMENT_VARIABLES = [
        'APP_CONFIG',
    ]
    for key in ENVIRONMENT_VARIABLES:
        os.environ[key] = environ.get(key, '')
    app = create_app(os.getenv('APP_CONFIG', 'production'))
    return app(environ, start_response)
