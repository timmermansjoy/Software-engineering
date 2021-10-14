from flask import Flask, render_template, request
from src.student import Student
import pandas as pd

app = Flask(__name__)

def get_students_from_csv(path):
    student_data = pd.read_csv(path)
    students = []
    for index, row in student_data.iterrows():
        students.append(Student(row.Number, row.Gender, row.GivenName, row.Surname, row.EmailAddress, row.GUID))
    return students


@app.route("/")
def index():
    title = "Software Engineering"
    return render_template("form.html", title=title)

@app.route("/groups", methods=['POST'])
def groups():
    title = "Groups"
    students = get_students_from_csv('temp/students.csv')
    return render_template("groups.html", title=title, students=students)

@app.route('/send', methods=['POST'])
def send():
    csv_content = request.files['csv_file']
    csv_content.save('temp/students.csv')
    students = get_students_from_csv('temp/students.csv')
    return render_template('form.html', students=students)
