from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def main():
    return render_template("main.html")
@app.route("/books")
def books():
    return render_template("books.html")
@app.route("/projects")
def projects():
    return render_template("projects.html")
@app.route("/archive")
def archive():
    return render_template("archive.html")
@app.route("/about")
def about():
    return render_template("about.html")
app.run(debug=True)