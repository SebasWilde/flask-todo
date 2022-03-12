"""
Auth views
"""
from flask import render_template

from forms import LoginForm
from . import auth


@auth.route('/login')
def login():
    login_form = LoginForm()
    context = {'login_form': login_form}
    return render_template('login.html', **context)
