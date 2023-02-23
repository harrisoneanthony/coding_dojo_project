from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

db = 'neighborhood_events_flask_app'

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) == 0 or len(user['last_name']) == 0 or len(user['email']) == 0 or len(user['password']) == 0 or len(user['confirm_password']) == 0:
            flash("All fields required")
            is_valid = False
        if len(user['first_name']) < 2:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address.")
            is_valid = False
        if not re.search("^(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[#$%&'()*+,-./:;<=>?@[\]^_`{|}~!]).*$", user['password']):
            flash("Password must be at least 8 characters and contain one number, one upper case character, and one special character.")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Passwords must match", 'confirm_password')
        return is_valid