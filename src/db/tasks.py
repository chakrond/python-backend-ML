import bson

from flask import current_app, g
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from datetime import datetime

def get_db():

    db = getattr(g, "_database", None)

    if db is None:

        db = g._database = PyMongo(current_app).db
       
    return db

# LocalProxy
db = LocalProxy(get_db)


# Database commands

def add_task(task_id, note):

    task = { 
        "task_id" : task_id,
        "note" : note,
        "date" : datetime.now()
    }

    return db.tasks.insert_one(task)

