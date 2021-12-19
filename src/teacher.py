from src.Person import Person
from src.Print_teacher import Print_teacher


class Teacher(Person):
    def __init__(self, number, gender, given_name, surname, email, GUID, group_number):
        self.number = number
        self.gender = gender
        self.given_name = given_name
        self.surname = surname
        self.email = email
        self.GUID = GUID
        self.group_number = group_number
        self.is_teacher = True
        self.print_strategy = Print_teacher()

    def __str__(self):
        return f"{self.number} {self.given_name} {self.surname}"

    def __repr__(self):
        return f"student object: {self.number}"

    def info(self):
        return "{} {} {} \t {} \t {}".format(
            self.number, self.given_name, self.surname, self.email, self.gender, "Teacher"
        )

    def name_print(self):
        x = "Ms." if self.gender == "Female" else "Mr."
        return "{} {}".format(x, self.surname)
