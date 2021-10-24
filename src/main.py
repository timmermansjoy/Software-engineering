import pandas as pd
import src


def main():
    helper = src.Helper()
    file_path = input("Give the path of the file: ")
    students = helper.get_students_from_csv(file_path)
    group_size = input("How many students will this group consist of?")
    number_of_groups = (
        len(students) / group_size if len(students) % group_size == 0 else (len(students) / group_size) + 1
    )
    groups = []
    for current_group_index, _ in enumerate(range(number_of_groups), start=1):
        students_in_group = []
        for j in range(group_size):
            student_first_name = input("give the first name of student {}".format(j + 1))
            student_last_name = input("give the last name of student {}".format(j + 1))
            student_email = input("give the e-mail of student {}".format(j + 1))
            student_number = input("give the number of student{}".format(j + 1))
            current_student = src.Student(student_first_name, student_last_name, student_email, student_number)
            students_in_group.append(current_student)
        groups.append(helper.make_group(students_in_group, group_size, current_group_index))
