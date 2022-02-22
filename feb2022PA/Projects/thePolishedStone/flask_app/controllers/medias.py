from flask_app import app
from flask import render_template, session
from flask_app.models.user import Users


@app.route('/media')
def media():
    if 'user_id' in session:
        data = {
        'id': session['user_id']
        }
        one_user = Users.get_profile(data)
        return render_template('media.html', current_user = one_user)
    else:
        return render_template('media.html', current_user = None, session = 0)