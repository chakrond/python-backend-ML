import os

from flask import Flask, render_template
from flask.json import JSONEncoder
from flask_cors import CORS
##from flask_bcrypt import Bcrypt
##from flask_jwt_extended import JWTManager

from bson import json_util, ObjectId
from datetime import datetime, timedelta

# Register Blueprints/Routers
from .routers.tasks import task_api

class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)


def create_app():

    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    STATIC_FOLDER = os.path.join(APP_DIR, '../public')
    TEMPLATE_FOLDER = os.path.join(APP_DIR, '../templates/views')

    app = Flask(__name__, static_folder=STATIC_FOLDER,
                template_folder=TEMPLATE_FOLDER,
                )
    CORS(app)
    app.json_encoder = MongoJsonEncoder
    app.register_blueprint(task_api)

    # Router to index
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')

    def serve(path):
        return render_template('index.html')

    return app