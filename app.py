# Activate Virtual Env
# .venv\Scripts\activate.bat

import os

# import configparser
from decouple import config

# flask app
from src.flask import create_app

# config = configparser.ConfigParser()
# config.read(os.path.abspath(os.path.join("./config/.ini")))

if __name__ == "__main__":
    app = create_app()
    app.config['DEBUG'] = True
    app.config['MONGO_URI'] = config('MONGODB_URI')

    app.run(threaded=True, port=5000)