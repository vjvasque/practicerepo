from flask_pymongo import PyMongo

mongo = PyMongo

class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    def safe(self):
        mongo.db.users.insert_one(self.__dict__)

    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({"email": email})
