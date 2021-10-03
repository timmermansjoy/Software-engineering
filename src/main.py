import pandas as pd
from group import Group
from student import Student


def get_students_from_csv(path):
    student_data = pd.read_csv(path)
    return [
        Student(
            row.firstname,
            row.lastname,
            row.email,
            row.gender,
            row.student_number,
        )
        for index, row in student_data.iterrows()
    ]


def make_group(student_list, group_size, group_number):
    if len(student_list) != group_size:
        print("The list of students you passed is not the correct group size")
    else:
        print("this group is the correct size")
        group = Group(student_list, group_number)
        for student in student_list:
            student.add_to_group(group_number)
        return group


def find_groupless_students(student_list):
    groupless = [student for student in student_list if not student.group_number]


def print_students(student_list):
    for student in student_list:
        print(student + "\n")


def main():
    file_path = input("Give the path of the file: ")
    newline = input("Give the newline character: ")
    delimiter = input("Give the delimiter character: ")
    quote_character = input("Give the quote character: ")
    students = get_students_from_csv(file_path, newline, delimiter, quote_character)
    group_size = input("How many students will this group consist of?")
    number_of_groups = len(students) / group_size if len(students) % group_size == 0 else (len(students) / group_size) + 1
    groups = []
    for current_group_index, _ in enumerate(range(number_of_groups), start=1):
        students_in_group = []
        for j in range(group_size):
            student_first_name = input("give the first name of student {}".format(j + 1))
            student_last_name = input("give the last name of student {}".format(j + 1))
            student_email = input("give the e-mail of student {}".format(j + 1))
            student_number = input("give the number of student{}".format(j + 1))
            current_student = Student(student_first_name, student_last_name, student_email, student_number)
            students_in_group.append(current_student)
        groups.append(make_group(students_in_group, group_size, current_group_index))
