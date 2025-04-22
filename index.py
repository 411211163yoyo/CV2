from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/job")
def job():
    return render_template("job.html")

@app.route("/future")
def future():
    return render_template("future.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

if __name__ == "__main__":
    app.run(debug=True)


