from flask import Flask

app = Flask(__name__)

# SQL Alchemy
from flask_sqlalchemy import SQLAlchemy

# An SQLite database named tasks.db is used. Three slashes
# tells you the file is in the same location as the files in this application
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"

# Ask SQLAlchemy to print all SQL queries
app.config["SQLALCHEMY_ECHO"] = True

# suppress the warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# Create a db object that is used to process the database
db = SQLAlchemy(app)

# get the view
from application import views

# get the db
from application.tasks import models

# get views from tasks
from application.tasks import views

# get auth
from application.auth import models

# get auth views
from application.auth import views

# logging
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please Login to use this Functionality"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Finally, the necessary database tables are created
db.create_all()