from flask import Flask, render_template, request
from Student import Student
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

@app.route('/send', methods=['POST'])
def send():
    csv_content = request.files['csv_file']
    students = get_students_from_csv(csv_content)
    return render_template('form.html', students=students)