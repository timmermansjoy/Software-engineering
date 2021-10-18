import pandas as pd
import src


class Helper:
    def __init__(self):
        self.students = None

    def setHelperStudents(self, students):
        self.students = students

    def get_students_from_csv(self, path):
        student_data = pd.read_csv(path)
        self.students =  [
            src.Student(
                row.firstname,
                row.lastname,
                row.email,
                row.gender,
                row.student_number,
            )
            for index, row in student_data.iterrows()
        ]

    def make_group(self, students_in_group, group_size, group_number):
        if len(students_in_group) != group_size:
            print("The list of students you passed is not the correct group size")
        else:
            print("this group is the correct size")
            group = src.Group(students_in_group, group_number)
            for student in students_in_group:
                student.add_to_group(group_number)
            return group

    def print_students(self):
        for student in self.students:
            x = student.name_print()
            print(x)

    def get_student_by_GUID(self, GUID):
        return [student for student in self.students if student.GUID == GUID]

    def get_student_by_id(self, id):
        return [student for student in self.students if student.id == id]

    def get_students_by_name(self, given_name):
        return [student for student in self.students if student.given_name == given_name]

    def get_groupless_students(self):
        return [student for student in self.students if not student.group_number]
