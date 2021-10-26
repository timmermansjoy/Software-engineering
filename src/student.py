class Student:
    def __init__(self, number, gender, given_name, surname, email, GUID):
        self.number = number
        self.gender = gender
        self.given_name = given_name
        self.surname = surname
        self.email = email
        self.GUID = GUID
        self.group_number = None

    def __str__(self):
        return f"{self.number} {self.given_name} {self.surname}"

    def __repr__(self):
        return f"student object: {self.number}"

    def add_to_group(self, group_number):
        self.group_number = group_number

    def info(self):
        return "{} {} {} \t {} \t {}".format(self.number, self.given_name, self.surname, self.email, self.gender)

    def name_print(self):
        return "{} {}".format(self.given_name, self.surname)
