from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, user_data):
        self.id = str(user_data['_id'])
        self.email = user_data['email']
        self.password_hash = user_data['password_hash']
        self.name = user_data['name']
        self.role = user_data.get('role', 'customer')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# MongoDB 'users' collection schema:
{
    "_id": ObjectId,
    "name": "string",
    "email": "string (unique)",
    "password_hash": "string",
    "role": "string ('customer' or 'admin')",
    "contact": "string (optional)",
    "address": "object (optional)",
    "created_at": "datetime"
}
