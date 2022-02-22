from flask_app import app
from flask import render_template

@app.route('/contact')
def contact_info():
    return render_template('contact.html')