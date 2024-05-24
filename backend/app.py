from flask import Flask
from flask_pymongo import PyMongo
from routes.posts import post_routes
from routes.users import user_routes

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/"
mongo = PyMongo(app)

app.register_blueprint(user_routes, url_prefix='/api')
app.register_blueprint(post_routes, url_prefix='/api')

if __name__ == '__main__':
    app.run()