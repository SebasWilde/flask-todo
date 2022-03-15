import firebase_admin
from firebase_admin import credentials, firestore

credentials = credentials.ApplicationDefault()
firebase_admin.initialize_app(credentials, {'projectId': 'flask-todo-65d34'})

db = firestore.client()


def get_users():
    return db.collection('users').get()


def get_todos(user_id):
    return db.collection('users').document(user_id).collection('todos').get()


def get_user(username):
    return db.collection('users').document(username).get()


def create_user(username, password):
    user_ref = db.collection('users').document(username)
    user_ref.set({'password': password})


def create_todo(username, todo_description):
    todo_collection_ref = (
        db.collection('users').document(username).collection('todos')
    )
    todo_collection_ref.add({'description': todo_description, 'done': False})


def delete_todo(username, todo_id):
    todo_ref = db.document(f'users/{username}/todos/{todo_id}')
    todo_ref.delete()


def update_todo(username, todo_id, done):
    todo_ref = db.document(f'users/{username}/todos/{todo_id}')
    todo_ref.update({'done': not done})
