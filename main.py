"""
Flask main
"""
import unittest

from flask import (
    render_template,
    request,
    make_response,
    redirect,
    session,
    flash,
    url_for,
)
from flask_login import login_required, current_user
from app import create_app
from app.firestore_service import get_users, get_todos, create_todo, \
    delete_todo, update_todo
from forms import TodoForm, DeleteForm, UpdateForm

app = create_app()


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = TodoForm()
    delete_form = DeleteForm()
    update_form = UpdateForm()
    context = {
        'user_ip': user_ip,
        'todos': get_todos(username),
        'username': username,
        'todo_form': todo_form,
        'delete_form': delete_form,
        'update_form': update_form
    }

    if todo_form.validate_on_submit():
        description = todo_form.description.data
        create_todo(username, description)
        flash('TODO was created')
        return redirect(url_for('hello'))

    return render_template('hello.html', **context)


@app.route('/todos/delete/<todo_id>', methods=['post'])
def delete_todo_view(todo_id):
    user_id = current_user.id
    delete_todo(user_id, todo_id)
    flash('TODO was deleted')
    return redirect(url_for('hello'))


@app.route('/todos/delete/<todo_id>/<int:done>', methods=['post'])
def update_todo_view(todo_id, done):
    user_id = current_user.id
    update_todo(user_id, todo_id, done)
    flash('TODO was updated')
    return redirect(url_for('hello'))
