# Activate Virtual Env
# .venv\Scripts\activate.bat

import os

# flask app
from src.flask import create_app

# Create app
app = create_app()

if __name__ == "__main__":
    
    app.config['DEBUG'] = True
    app.config['MONGO_URI'] = os.environ['MONGODB_URI']
    app.run(threaded=True, port=5000)