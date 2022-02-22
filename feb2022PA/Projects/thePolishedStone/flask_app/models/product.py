from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models import product

class Product:
    db_name = "thepolishedstone"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.prod_desc = data['prod_desc']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.materials = []
        self.user = []
        self.pictures = []

    @staticmethod
    def validate_product(product):
        is_valid = True
        if len(product['name']) < 1:
            flash("Must provide a name for this product.")
            is_valid = False
        if len(product['material_id']) < 1:
            flash("Must provide a material for this product.")
            is_valid = False
        if len(product['prod_desc']) < 10:
            flash("Must provide a description longer than 20 characters.")
            is_valid = False
        if len(product['price']) < 0.01:
            flash("Please provide a price for this product.")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_edit(product):
        is_valid = True
        if len(product['name']) < 1:
            flash("Must provide a name for this product.")
            is_valid = False
        if len(product['prod_desc']) < 10:
            flash("Must provide a description longer than 20 characters.")
            is_valid = False
        if len(product['price']) < 0.01:
            flash("Please provide a price for this product.")
            is_valid = False
        return is_valid

    @classmethod
    def save_product(cls, data):
        query = "INSERT INTO products (name, prod_desc, price, created_at, updated_at, user_id, material_id) VALUES (%(name)s, %(prod_desc)s, %(price)s, NOW(), NOW(), %(user_id)s, %(material_id)s);"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    @classmethod
    def user_products(cls):
        query = "SELECT * FROM users LEFT JOIN products ON user_id = users.id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        all_products = []
        for db_row in results:
            product_data = {
                'id': db_row['products.id'],
                'name': db_row['name'],
                'prod_desc': db_row['prod_desc'],
                'price': db_row['price'],
                'created_at': db_row['created_at'],
                'updated_at': db_row['updated_at'],
                'material_id': db_row['material_id']
            }
            one_product = cls(product_data)
            user_data = {
                'id': db_row['id'],
                'username':db_row['username'],
                'first_name': db_row['first_name'],
                'last_name': db_row['last_name'],
                'email': db_row['email'],
                'password': db_row['password'],
                'dob': db_row['dob'],
                'fav_stone': db_row['fav_stone'],
                'prof': db_row['prof'],
                'hobbies': db_row['hobbies'],
                'descr': db_row['descr'],
                'bio': db_row['bio'],
                'created_at': db_row['created_at'],
                'updated_at': db_row['updated_at']
            }
            one_user = user.Users(user_data)
            one_product.user = one_user
            all_products.append(one_product)
        return all_products

    @classmethod
    def get_product(cls, data):
        query = "SELECT * FROM products WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def update_product(cls, data):
        query = "UPDATE products SET name=%(name)s, prod_desc=%(prod_desc)s, price=%(price)s, updated_at=NOW() WHERE name = %(name)s"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    @classmethod
    def delete_product(cls, data):
        query = "DELETE FROM products WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)