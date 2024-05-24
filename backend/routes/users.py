from flask import Blueprint, request, jsonify
from models.user import User

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['POST'])

def create_user():
    data = request.get_json()
    user = User(data['name'], data['email'])
    user.save()
    return jsonify({"message": "User created successfully"}), 201

@user_routes.route('/users/<email>', methods=['GET'])
def get_user(email):
    user = User.find_by_email(email)
    if user:
        return jsonify(user), 200
    return jsonify({"message", "Could not find user"}), 404
