from flask import Blueprint, render_template, request, redirect, url_for
from . import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    tasks = mongo.db.tasks.find()  # Fetch tasks from MongoDB
    return render_template('index.html', tasks=tasks)

@main.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('name')
    if task_name:
        mongo.db.tasks.insert_one({'name': task_name})
    return redirect(url_for('main.index'))

@main.route('/delete/<task_id>')
def delete_task(task_id):
    mongo.db.tasks.delete_one({'_id': mongo.ObjectId(task_id)})
    return redirect(url_for('main.index'))
