import os
from flask import Flask, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
import pandas as pd
import src


app = Flask(__name__)
app.config["UPLOAD_EXTENSIONS"] = [".csv", ".txt"]
app.config["UPLOAD_PATH"] = "uploads"


#! We have this in helpers? can this be deleted?
def get_students_from_csv(path):
    student_data = pd.read_csv(path)
    students = []
    for index, row in student_data.iterrows():
        students.append(src.Student(row.Number, row.Gender, row.GivenName, row.Surname, row.EmailAddress, row.GUID))
    return students


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
        uploaded_file.save(os.path.join(app.config["UPLOAD_PATH"], filename))
    return redirect(url_for("index"))


@app.route("/test")
def test():
    return render_template("test.html", title=title)


@app.route("/groups", methods=["POST"])
def groups():
    title = "Groups"
    students = get_students_from_csv("temp/students.csv")
    return render_template("groups.html", title=title, students=students)


@app.route("/send", methods=["POST"])
def send():
    csv_content = request.files["csv_file"]
    csv_content.save("temp/students.csv")
    students = get_students_from_csv("temp/students.csv")
    return render_template("form.html", students=students)
