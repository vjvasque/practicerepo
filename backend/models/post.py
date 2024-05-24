from flask_pymongo import PyMongo

mongo = PyMongo

class User:
    def __init__(self, title, content, user_id) -> None:
        self.title = title
        self.content = content
        self.user_id = user_id

    def safe(self):
        mongo.db.posts.insert_one(self.__dict__)

    @staticmethod
    def find_by_user(user_id):
        return list(mongo.db.posts.find({"user_id": user_id}))
