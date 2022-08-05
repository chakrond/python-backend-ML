import os
# import configparser
from src.app import create_app
from decouple import config

# config = configparser.ConfigParser()
# config.read(os.path.abspath(os.path.join("./config/.ini")))

if __name__ == "__main__":
    app = create_app()
    app.config['DEBUG'] = True
    app.config['MONGO_URI'] = config('MONGODB_URI')

    app.run()