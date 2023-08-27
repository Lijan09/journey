from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    name = "Lijan"
    return render_template("about.html", name = name)

@app.route("/rick")
def rick():
    return render_template("rick.html")

app.run(debug=True)