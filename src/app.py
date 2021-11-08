import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import pandas as pd
import src


app = Flask(__name__)
app.config["UPLOAD_EXTENSIONS"] = [".csv", ".txt"]
app.config["UPLOAD_PATH"] = "uploads"
helper = src.Helper()


# @app.route("/")
# def index():
#     title = "Software Engineering"
#     return render_template("form.html", title=title)


title = "ClassMate"


@app.route("/")
def index():
    return render_template("index.html", title=title)


@app.route("/", methods=["POST"])
def upload_files():
    uploaded_file = request.files["file"]
    filename = secure_filename(uploaded_file.filename)
    if filename != "":
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
            return "Invalid file format", 400
    
        people = helper.get_people_from_csv(uploaded_file)
        ## TODO: the students variable should be a list of Student objects. Instead this is empty.
        print(people)
    ## TODO: redirect isnt redirecting.
    ## TODO: redirect isnt redirectingk.
    return redirect(url_for("test", students=people))


@app.route("/test", methods=["GET"])
def test(students=[]):
    print(helper.people)
    return render_template("test.html", title=title, students=helper.people)


@app.route("/groups", methods=["POST"])
def groups():
    students = helper.get_people_from_csv("temp/students.csv")
    return render_template("groups.html", title=title, students=helper.people)


@app.route("/send", methods=["POST"])
def send():
    csv_content = request.files["csv_file"]
    csv_content.save("temp/students.csv")
    return render_template("form.html", students=helper.people)


if __name__ == "__main__":
    app.run(debug=True)
