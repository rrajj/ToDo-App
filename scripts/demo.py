from flask import Flask, render_template
app = Flask(__name__)

name = "John Doe"
list = [25, 50, 75, 100]
dict = {"a": 1, "b": 2, "c": 3, "d": 4}

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/demo")
def demo():
    return render_template("demo.html", name=name, list=list, dict=dict)

if __name__ == "__main__":
    app.run(debug = True)