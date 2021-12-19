import os
from flask import Flask, render_template, request, redirect, url_for, make_response
from src.CsvReader import CsvReader
from werkzeug.utils import secure_filename
import pandas as pd
import src
from src import Student
from src.EmailParser import EmailParser
from src.Populator import Populator
from src.PersonFinder import PersonFinder
from src.GroupFactory import GroupFactory

app = Flask(__name__)
app.config["UPLOAD_EXTENSIONS"] = [".csv", ".txt"]

title = "ClassMate"
populator = Populator()
personFinder = PersonFinder(populator)
groupFactory = GroupFactory(populator)


@app.route("/")
def index():
    return render_template("index.html", title=title)


@app.route("/uploader", methods=["GET"])
def show_view():
    if EmailParser.is_teacher(current_user):
        return


@app.route("/uploader", methods=["POST"])
def upload_view():
    global current_user
    current_user = request.form.get("email")
    if not EmailParser.is_valid(current_user):
        return render_template(
            "index.html", title=title, error="Please make sure you are using your organization's email."
        )

    if EmailParser.is_student(current_user):
        return render_template("find_class.html")

    if EmailParser.is_teacher(current_user):
        filename = EmailParser.get_filename_from_email(current_user)

        if os.path.exists(f"./data/{filename}"):
            people = populator.populate_people(filename)
            person = personFinder.get_person_by_email(filename, current_user)
            return render_template(
                "students.html", title=title, students=people, message=person.print_strategy.print_person(person)
            )

        return render_template("upload.html", title=title, email=current_user)


@app.route("/find_class", methods=["POST"])
def find_class():
    teacher = request.form.get("email")

    if not EmailParser.is_teacher(teacher):
        return render_template("find_class.html", title=title, error="Please enter a valid teacher email.")

    filename = EmailParser.get_filename_from_email(teacher)
    if not os.path.exists(f"./data/{filename}"):
        return render_template(
            "find_class.html", title=title, error="Your teacher has not uploaded your classfile yet :("
        )

    people = populator.populate_people(filename)
    student = personFinder.get_person_by_email(filename, current_user)
    if not student:
        return render_template(
            "find_class.html", title=title, error="Your teacher has not uploaded your classfile yet :("
        )

    if student.group_number == 0:
        return render_template(
            "make_group.html",
            title=title,
            students=people,
            teacher=teacher,
            message=student.print_strategy.print_person(student),
        )
    members = groupFactory.get_group_members(student.group_number, filename)
    return render_template(
        "show_group.html", title=title, students=members, message=student.print_strategy.print_person(student)
    )


@app.route("/save_group", methods=["POST"])
def save_group():
    student1 = request.form.get("student1")
    student2 = request.form.get("student2")
    student3 = request.form.get("student3")
    teacher = request.form.get("teacher")
    filename = EmailParser.get_filename_from_email(teacher)
    people = populator.populate_people(filename)
    try:
        students = [
            personFinder.get_person_by_email(filename, student1),
            personFinder.get_person_by_email(filename, student2),
            personFinder.get_person_by_email(filename, student3),
            personFinder.get_person_by_email(filename, current_user),
        ]
        group = groupFactory.create_group(students, filename)
        return render_template(
            "show_group.html",
            title=title,
            students=group.get_group_members(),
            message=students[3].print_strategy.print_person(students[3]),
        )
    except Exception as e:
        print(e)
        return render_template("make_group.html", title=title, students=people, teacher=teacher, error="Invalid group")


@app.route("/upload", methods=["POST"])
def upload_files():
    uploaded_file = request.files["file"]
    filename = secure_filename(uploaded_file.filename)
    if filename != "":
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
            return "Invalid file format", 400
        filename = EmailParser.get_filename_from_email(current_user)
        uploaded_file.save(os.path.join("./data/", filename))
    return redirect(url_for("students"))


@app.route("/students", methods=["POST", "GET"])
def students():
    filename = EmailParser.get_filename_from_email(current_user)
    people = populator.populate_people(filename)
    return render_template("students.html", title=title, students=people)


@app.route("/send", methods=["POST"])
def send():
    csv_content = request.files["csv_file"]
    csv_content.save("temp/students.csv")
    people = populator.populate_people(csv_content)
    return render_template("form.html", students=people)


if __name__ == "__main__":
    app.run(debug=True)
