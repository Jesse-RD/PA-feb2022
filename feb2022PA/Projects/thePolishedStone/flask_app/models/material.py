from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import product, user

class Materials:
    db_name = "thepolishedstone"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.product = []
        self.pictures = []

    @classmethod
    def all_materials(cls):
        query = "SELECT * FROM materials;"
        results = connectToMySQL(cls.db_name).query_db(query)
        return results

    @classmethod
    def all_product_materials(cls, data):
        query = "SELECT * FROM materials LEFT JOIN products ON products.material_id = materials.id WHERE materials.id = %(material_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        all_products = []
        for db_row in results:
            product_data = {
                'id': db_row['products.id'],
                'name': db_row['products.name'],
                'prod_desc': db_row['prod_desc'],
                'price': db_row['price'],
                'created_at': db_row['created_at'],
                'updated_at': db_row['updated_at'],
                'user_id': db_row['user_id']
            }
            one_product = cls(product_data)
            material_data = {
                'id': db_row['id'],
                'name': db_row['name']
            }
            one_material = cls(material_data)
            one_product = product.Product(product_data)
            one_material.product = one_product
            all_products.append(one_product)
        return all_products

# Add additional material integration before launching ecommerce to public

    @classmethod
    def add_material(cls, data):
        query = "INSERT INTO materials (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        return results

    @classmethod
    def user_products(cls, data):
        query = "SELECT * FROM products LEFT JOIN users ON products.user_id = users.id;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        all_materials = []
        for db_row in results:
            material_data = {
                'id': db_row['id'],
                'name': db_row['name'],
                'user_id': db_row['users.id'],
                'product_id': db_row['products.id']
            }
            one_material = cls(material_data)
            product_data = {
                'id': db_row['id'],
                'name': db_row['name'],
                'prod_desc': db_row['prod_desc'],
                'price': db_row['price'],
                'created_at': db_row['created_at'],
                'updated_at': db_row['updated_at'],
                'user_id': db_row['materials.user_id']
            }
            one_product = cls(product_data)
            user_data = {
                'id': db_row['users.id'],
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
                'created_at': db_row['users.created_at'],
                'updated_at': db_row['users.updated_at']
            }
            one_user = user.Users(user_data)
            one_product.user = one_user
            one_product = product.Product(product_data)
            one_material.product = one_product
            all_materials.append(one_product)
        return all_materials