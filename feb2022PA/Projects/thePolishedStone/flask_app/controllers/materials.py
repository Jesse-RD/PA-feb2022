from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.product import Product
from flask_app.models.material import Materials
from flask_app.models.user import Users

@app.route('/store')
def view_store():
    if 'user_id' in session:
        data = {
        'id': session['user_id']
        }
        one_user = Users.get_profile(data)
        return render_template('materials.html', current_user = one_user)
    else:
        return render_template('materials.html', current_user = False, session = 0)

@app.route('/add_material', methods=['POST'])
def new_material():
    mat_data = {
        'name': request.form['material'],
        'user_id': session['user_id']
    }
    Materials.add_material(mat_data)
    return redirect('/admin')