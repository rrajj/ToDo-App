from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators


class TaskForm(FlaskForm):
    # name of the task
    # text field must be at least two lengths
    # Validation errors are stored in the form field by field in a variable named below each field `errors`
    name = StringField("Task Name", [validators.Length(min=2)])

    # field that allows user to specify task done or not
    done = BooleanField("Done")

    class Meta:
        # turns off recourse to cross-site request forgery attacks
        csrf = False
