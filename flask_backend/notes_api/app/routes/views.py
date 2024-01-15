from flask import Blueprint, request, jsonify
from ..models.models import db, User, Note

views = Blueprint('views', __name__)

# Views

@views.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify({'users': [user.to_dict() for user in users]})

@views.route('/notes', methods=['GET'])
def get_notes():
    notes = Notes.query.all
    return jsonify({'notes': [note.to_dict() for note in notes]})

@views.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user_to_dict())

@views.route('/note/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = Note.query.get_or_404(note_id)
    return jsonify(note.to_dict())

# Functions for me
def user_to_dict(user):
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email
    }
    
def note_to_dict(note):
    return {
        'id': note.id,
        'title': note.title,
        'content': note.content,
        'created_at': note.created_at
        'user_id': note.user_id
    }
    
User.to_dict = user_to_dict
Note.to_dict = note_to_dict