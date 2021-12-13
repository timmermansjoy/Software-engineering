from Person import Person
from Print_student import Print_student


class Student(Person):
    def __init__(self, number, gender, given_name, surname, email, GUID):
        self.number = number
        self.gender = gender
        self.given_name = given_name
        self.surname = surname
        self.email = email
        self.GUID = GUID
        self.group_number = None
        self.is_teacher = False
        self.print_strategy = Print_student()

    def __str__(self):
        return "{} {} {}".format(self.number, self.given_name, self.surname)

    def __repr__(self):
        return "student object: {}".format(self.number)

    def info(self):
        return "{} {} {} \t {} \t {}".format(
            self.number, self.given_name, self.surname, self.email, self.gender, "Student"
        )

    def name_print(self):
        return "{} {}".format(self.given_name, self.surname)

    def add_to_group(self, group_number):
        self.group_number = group_number
