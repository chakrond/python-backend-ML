from flask import Blueprint, request, jsonify
from flask_cors import CORS

from db.db_tasks import add_task
from utils.expect import expect


task_api = Blueprint(
    'task_api', 'task_api', url_prefix='/task/')

CORS(task_api)

@task_api.route('/add', methods=['POST'])
def add():

    req = request.get_json()

    # make POST request to db
    try:

        task_id = expect(req.get('task_id'), str, 'task_id')
        note = expect(req.get('note'), str, 'note')
        add_task(task_id, note)

        return jsonify({"stat": "task added!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400
