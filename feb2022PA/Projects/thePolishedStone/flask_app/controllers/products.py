from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.product import Product
from flask_app.models.user import Users
from flask_app.models.material import Materials

import os

from flask import Flask, flash, url_for, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:/Users/jesse/Documents/CodingDojo/Projects/feb2022PA/Projects/thePolishedStone/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    user_id = session['user_id']
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(f'/profile/{user_id}')
        return redirect(f'/profile/{user_id}')

@app.route('/new_product/<int:user_id>')
def create_product(user_id):
    if 'user_id' not in session:
        return redirect('/')
    user_id = session['user_id']
    return render_template('new_product.html', current_user = user_id)

@app.route('/process_product/<int:user_id>', methods=['POST'])
def process_product(user_id):
    user_id = session['user_id']
    if not Product.validate_product(request.form):
        return redirect(f'/new_product/{user_id}')
    prod_data = {
        'name': request.form['name'],
        'prod_desc': request.form['prod_desc'],
        'price': request.form['price'],
        'user_id': session['user_id'],
        'material_id': request.form['material_id']
    }
    Product.save_product(prod_data)
    return redirect(f'/profile/{user_id}')

@app.route('/edit_product/<int:user_id>/<product_id>')
def edit_product(user_id, product_id):
    user_id = session['user_id']
    data = {
        'id': user_id
    }
    prod_data = {
        'id': product_id
    }
    one_product = Product.get_product(prod_data)
    return render_template('edit_product.html', current_user = user_id, product = one_product)

@app.route('/update_product/<int:user_id>/<product_id>', methods=['POST'])
def update_product(user_id, product_id):
    user_id = session['user_id']
    if 'user_id' not in session:
        return redirect('/')
    if not Product.validate_edit(request.form):
        return redirect(f'/edit_product/{user_id}/{product_id}')
    data = {
        'id': product_id,
        'name': request.form['name'],
        'prod_desc': request.form['prod_desc'],
        'price': request.form['price'],
        'user_id': session['user_id']
    }
    Product.update_product(data)
    return redirect(f'/profile/{user_id}')

@app.route('/delete_product/<int:user_id>/<product_id>', methods=['POST'])
def delete_product(user_id, product_id):
    user_id = session['user_id']
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': product_id
    }
    Product.delete_product(data)
    return redirect(f'/profile/{user_id}')

@app.route('/<material_id>/products')
def material_products(material_id):
    if 'user_id' in session:
        user_data = {
            'id': session['user_id']
        }
        mat_data = {
            'material_id': material_id
        }
        one_user = Users.get_profile(user_data)
        all_products = Materials.all_product_materials(mat_data)
        return render_template('products.html', current_user = one_user, all_products = all_products, current_mat = material_id)
    else:
        mat_data = {
            'material_id': material_id
        }
        all_products = Materials.all_product_materials(mat_data)
        return render_template('products.html', current_user = False, session = 0, all_products = all_products, current_mat = material_id)

@app.route('/<material_id>/<product_id>/details')
def single_product(product_id, material_id):
    if 'user_id' in session:
        user_id = session['user_id']
        product_data = {
            'id': product_id
        }
        mat_data = {
            'material_id': material_id
        }
        single_product = Product.get_product(product_data)
        return render_template('/single_product.html', user = user_id, product = single_product, current_mat = material_id)
    else:
        product_data = {
            'id': product_id
        }
        mat_data = {
            'material_id': material_id
        }
        Materials.all_product_materials(mat_data)
        single_product = Product.get_product(product_data)
        return render_template('/single_product.html', product = single_product, user = False, session = 0, current_mat = material_id)