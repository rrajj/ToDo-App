from flask_wtf import FlaskForm
from wtforms import StringField


class TaskForm(FlaskForm):
    name = StringField("Task Name")

    class Meta:
        # turns off recourse to cross-site request forgery attacks
        csrf = False
