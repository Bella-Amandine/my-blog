from flask import Flask 
from config import config_options
from flask_sqlalchemy import SQLAlchemy

#Initializing flask extension
db = SQLAlchemy()

def create_app(config_name):

    #Initializing application
    app = Flask(__name__)

    #Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Initializing flask extension
    db.init_app(app)

    return app