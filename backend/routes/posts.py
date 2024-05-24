from flask import Blueprint, request, jsonify
from models.post import Post

post_routes = Blueprint('post_routes', __name__)

@post_routes.route('/posts', methods=['POST'])

def create_posts():
    data = request.get_json()
    post = Post(data['title'], data['content'], data['user_id'])
    post.save()
    return jsonify({"message": "Post created successfully"}), 201

@post_routes.route('/posts/<user_id>', methods=['GET'])
def get_post(user_id):
    posts = Post.find_by_user(user_id)
    return jsonify(posts), 200
