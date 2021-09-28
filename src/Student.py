class Student:
    def __init__(self, first_name, last_name, email, gender, student_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.student_number = student_number
        self.gender = gender
        self.group_number = None

    def add_to_group(self, group_number):
        self.group_number = group_number

    def info(self):
        return "{} {} {} \t {} \t {}".format(self.student_number, self.last_name, self.first_name, self.email, self.gender)
