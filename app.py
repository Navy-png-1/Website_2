from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def main():
    return render_template("main.html")
@app.route("/projects")
def projects():
    return render_template("projects.html")
app.run(debug=True)