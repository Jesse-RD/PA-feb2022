import re

from flask import flash

from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

class Users:
    db_name = "thepolishedstone"
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.dob = data['dob']
        self.hobbies = data['hobbies']
        self.fav_stone = data['fav_stone']
        self.prof = data['prof']
        self.descr = data['descr']
        self.bio = data['bio']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.products = []
        self.pictures = []

    @staticmethod
    def validate_register(user):
        is_valid = True
        users_with_email = Users.get_by_email({'email': user['email']})
        if users_with_email:
            flash("There is already an account associated with this email.")
            is_valid = False
        if len(user['username']) < 2:
            flash("Please provide a display name.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must have more than 8 characters.")
            is_valid = False
        if (user['password']) != (user['r_password']):
            flash("Repeated passwords must match!")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(user):
        is_valid = True
        users_with_email = Users.get_by_email({'email': user['email']})
        if not users_with_email:
            flash("Invalid Email/Password. Please Try Again.")
            is_valid = False
        if users_with_email:
            if len(user['email']) < 8:
                flash("Invalid Email/Password. Please Try Again.")
                is_valid = False
            if len(user['password']) < 8:
                flash("Invalid Email/Password. Please Try Again.")
                is_valid = False
        return is_valid

    @classmethod
    def get_profile(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if not results:
            return False
        one_user = cls(results[0])
        return one_user

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (username, email, password, first_name, last_name, hobbies, fav_stone, created_at, updated_at) VALUES (%(username)s, %(email)s, %(password)s, %(first_name)s, %(last_name)s, %(hobbies)s, %(fav_stone)s, NOW(), NOW());"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = "UPDATE users SET username=%(username)s, first_name=%(first_name)s, last_name=%(last_name)s, hobbies=%(hobbies)s, fav_stone=%(fav_stone)s, dob=%(dob)s, prof=%(prof)s, descr=%(descr)s, bio=%(bio)s, updated_at=NOW() WHERE id = %(id)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results







