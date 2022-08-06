from flask import Blueprint, request, jsonify
from flask_cors import CORS

from ..db.tasks import add_task
from ..utils.expect import expect
from ..pytorch.model import get_prediction

# Blueprint
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


# Prediction test
@task_api.route('/predict', methods=['POST'])
def predict():

    if request.method == 'POST':

        try:

            file = request.files['file']
            img_bytes = file.read()
            class_id, class_name = get_prediction(image_bytes=img_bytes)
            return jsonify({'class_id': class_id, 'class_name': class_name})

        except Exception as e:
            return jsonify({"error": str(e)}), 400
