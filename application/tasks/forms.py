from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField


class TaskForm(FlaskForm):
    # name of the task
    name = StringField("Task Name")

    # field that allows user to specify task done or not
    done = BooleanField("Done")

    class Meta:
        # turns off recourse to cross-site request forgery attacks
        csrf = False
