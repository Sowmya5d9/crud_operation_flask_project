from flask import Blueprint, request, jsonify
from models import get_all_items, add_item, update_item, delete_item
from ml_model import predict_value

item_bp = Blueprint('item_bp', __name__)

# READ all items
@item_bp.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(get_all_items())

# CREATE item
@item_bp.route('/api/items', methods=['POST'])
def create_item():
    data = request.json
    name = data.get("name")
    value = data.get("value")

    prediction = predict_value(value)
    item = add_item(name, value, prediction)

    return jsonify(item)

# UPDATE item
@item_bp.route('/api/items/<int:item_id>', methods=['PUT'])
def update(item_id):
    data = request.json
    name = data.get("name")
    value = data.get("value")

    prediction = predict_value(value)
    item = update_item(item_id, name, value, prediction)

    return jsonify(item if item else {"error": "Item not found"})

# DELETE item
@item_bp.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete(item_id):
    delete_item(item_id)
    return jsonify({"message": "Deleted successfully"})