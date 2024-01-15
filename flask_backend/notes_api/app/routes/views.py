from flask import Blueprint, jsonify
from ..models.models import User, Note

views = Blueprint('views', __name__)

@views.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])