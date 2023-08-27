import os

from flask import Flask 

def create_app(test_config=NONE):
    app = Flask(__name__, istance_relative_config = True)
    app.config.from.mapping( SECRET_KEY = 'lallavesecreta', DATABASE = os.path.join(app.instance_path, 'flask.sqlite'),)

