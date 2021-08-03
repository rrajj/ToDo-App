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

# Finally, the necessary database tables are created
db.create_all()