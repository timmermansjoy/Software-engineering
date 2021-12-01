import os
from flask import Flask, render_template, request, redirect, url_for, make_response
from werkzeug.utils import secure_filename
import pandas as pd
import src
from src import student

helper = src.Helper()

app = Flask(__name__)
app.config["UPLOAD_EXTENSIONS"] = [".csv", ".txt"]
app.config["UPLOAD_PATH"] = "uploads"
helper = src.Helper()


# @app.route("/")</form></form>
# def in<</button>/button>dex():
#     title = "Software Engineering"
#     return render_template("form.html", title=title)


title = "ClassMate"


@app.route("/")
def index():
    return render_template("index.html", title=title)


@app.route("/uploader", methods=["GET"])
def show_view():
    if current_user.split("@")[1] == "pxl.be":
        return


@app.route("/uploader", methods=["POST"])
def upload_view():
    global current_user
    current_user = request.form.get("email")
    message = ""
    if "student.pxl.be" in current_user:
        return render_template("make_groups.html")
    elif "pxl.be" in current_user:
        name = current_user.split("@")[0].strip(".")
        if os.path.exists(f"./data/{name}.csv"):
            helper.get_people_from_csv(f"{name}.csv")
            return render_template("students.html", title=title, students=helper.people)
        return render_template("upload.html", title=title, email=current_user, message=message)
    else:
        message = "INVALID EMAIL"
        return render_template(
            "index.html", title=title, error="Please make sure you are using your organization's email."
        )


@app.route("/upload", methods=["POST"])
def upload_files():
    uploaded_file = request.files["file"]
    filename = secure_filename(uploaded_file.filename)
    if filename != "":
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
            return "Invalid file format", 400
        filename = current_user.split("@")[0].strip(".") + ".csv"
        uploaded_file.save(os.path.join("./data/", filename))
    return redirect(url_for("students"))


@app.route("/students", methods=["POST", "GET"])
def students():
    filename = current_user.split("@")[0].strip(".") + ".csv"
    return render_template("students.html", title=title, students=helper.people)


@app.route("/send", methods=["POST"])
def send():
    csv_content = request.files["csv_file"]
    csv_content.save("temp/students.csv")
    return render_template("form.html", students=helper.people)


if __name__ == "__main__":
    app.run(debug=True)
