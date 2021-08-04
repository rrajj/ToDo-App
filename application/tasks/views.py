from application import app, db
from flask import render_template, request, redirect, url_for
from application.tasks.models import Task
from application.tasks.forms import TaskForm

@app.route("/tasks", methods=["GET"])
def tasks_index():
    return render_template("list.html", tasks = Task.query.all())


@app.route("/tasks/new/")
def tasks_form():
    return render_template("new.html", form=TaskForm())


@app.route("/tasks/<task_id>/", methods=["POST"])
def tasks_set_done(task_id):
    t = Task.query.get(task_id)
    t.done = True
    db.session().commit()
    return redirect(url_for("tasks_index"))


@app.route("/tasks/", methods=["POST"])
def task_create():
    form = TaskForm(request.form)

    if not form.validate():
        return render_template("new.html", form=form)

    # get details from form
    t = Task(form.name.data)
    t.done = form.done.data

    db.session().add(t)
    db.session().commit()

    # return "Hello World!!"

    # redirect to a page where all the tasks are listed
    return redirect(url_for("tasks_index"))
