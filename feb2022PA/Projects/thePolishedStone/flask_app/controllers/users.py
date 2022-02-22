from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import Users
from flask_app.models.product import Product
from flask_app.models.material import Materials


from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/admin')
def admin():
    data = {
    'id': session['user_id']
    }
    one_user = Users.get_profile(data)
    materials = Materials.all_materials()
    if one_user.email != "admin@email.com":
        return redirect ('/')
    else:
        return render_template('admin.html', current_user = one_user, materials = materials)

@app.route('/')
def home():
    if 'user_id' in session:
        data = {
        'id': session['user_id']
        }
        one_user = Users.get_profile(data)
        print("*******")
        print(one_user)
        return render_template('home.html', current_user = one_user)
    else:
        return render_template('home.html', current_user = False, session = 0)

@app.route('/register')
def create_user():
    if 'user_id' in session:
        data = {
        'id': session['user_id']
        }
        one_user = Users.get_profile(data)
        return render_template('register.html', current_user = one_user)
    else:
        return render_template('register.html', current_user = False, session = 0)

@app.route('/process_user', methods=['POST'])
def process_user():
    if not Users.validate_register(request.form):
        return redirect('/register')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'username': request.form['username'],
        'email': request.form['email'],
        'password': pw_hash,
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'hobbies': request.form['hobbies'],
        'fav_stone': request.form['fav_stone']
    }
    user_id = Users.save(data)
    session['user_id'] = user_id
    return redirect('/')

@app.route('/login')
def login_page():
    if 'user_id' in session:
        data = {
        'id': session['user_id']
        }
        one_user = Users.get_profile(data)
        return render_template('home.html', current_user = one_user)
    else:
        return render_template('login.html', current_user = False, session = 0)

@app.route('/process_login', methods=["POST"])
def user_login():
    if not Users.validate_login(request.form):
        return redirect('/login')
    data = {'email': request.form['email']}
    user_with_email = Users.get_by_email(data)
    user_id = user_with_email.id
    if 'user_id' in session:
        return redirect(f'/profile/{user_id}')
    if user_with_email == False:
        flash("Invalid Email/Password.")
        return redirect('/')
    if not bcrypt.check_password_hash(user_with_email.password, request.form['password']):
        flash("Invalid Email/Password.")
        return redirect('/')
    session['user_id'] = user_with_email.id
    return redirect('/')

@app.route('/profile/<int:user_id>')
def user_profile(user_id):
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id': session['user_id'],
        'user_id': user_id
    }
    products = Product.user_products()
    one_user = Users.get_profile(user_data)
    if one_user == False:
        return redirect('/login')
    return render_template('profile.html', user_profile = one_user, all_products = products)

@app.route('/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    data = {
        'id': user_id,
        'username': request.form['username'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'dob': request.form['dob'],
        'fav_stone': request.form['fav_stone'],
        'prof': request.form['prof'],
        'hobbies': request.form['hobbies'],
        'descr': request.form['descr'],
        'bio': request.form['bio']
    }
    Users.edit(data)
    return redirect(f'/profile/{user_id}')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')

@app.route('/contact')
def contact():
    if 'user_id' in session:
        data = {
        'id': session['user_id']
        }
        one_user = Users.get_profile(data)
        return render_template('contact.html', current_user = one_user)
    else:
        return render_template('contact.html', current_user = False, session = 0)