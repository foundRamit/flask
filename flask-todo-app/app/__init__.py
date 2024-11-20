from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/todo_db'
    app.config['SECRET_KEY'] = 'your-secret-key'

    mongo.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
