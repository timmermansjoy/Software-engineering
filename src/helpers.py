import pandas as pd
from student import Student
from teacher import Teacher
from group import Group
from PersonFactory import PersonFactory


class Helper:
    def __init__(self):
        self.people = []
        self.person_factory = PersonFactory()

    def set_helper_people(self, people):
        self.people = people

    def get_people_from_csv(self, filename):
        self.people = []
        person_data = pd.read_csv(f"./data/{filename}")
        for _, row in person_data.iterrows():
            if row["EmailAddress"].split("@")[1] == "student.pxl.be":
                person = self.person_factory.create_person(
                    "STUDENT",
                    number=row["Number"],
                    given_name=row["GivenName"],
                    surname=row["Surname"],
                    email=row["EmailAddress"],
                    gender=row["Gender"],
                    GUID=row["GUID"],
                )
                print("Student found!")
                self.people.append(person)
            elif row["EmailAddress"].split("@")[1] == "pxl.be":
                person = self.person_factory.create_person(
                    "TEACHER",
                    number=row["Number"],
                    given_name=row["GivenName"],
                    surname=row["Surname"],
                    email=row["EmailAddress"],
                    gender=row["Gender"],
                    GUID=row["GUID"],
                )
                print("Teacher found!")
                self.people.append(person)
            else:
                raise Exception("Invalid email???? :(((")

        return self.people

    def make_group(self, students_in_group, group_size, group_number):
        if len(students_in_group) != group_size:
            print("The list of students you passed is not the correct group size")
        else:
            print("this group is the correct size")
            group = Group(students_in_group, group_number)
            for student in students_in_group:
                student.add_to_group(group_number)
            return group

    def print_people(self):
        for person in self.people:
            x = person.name_print()
            print(x)

    def get_person_by_GUID(self, GUID):
        return [person for person in self.people if person.GUID == GUID]

    def get_person_by_id(self, id):
        return [person for person in self.people if person.id == id]

    def get_people_by_name(self, given_name):
        return [person for person in self.people if person.given_name == given_name]
    
    def get_person_by_email(self, email):
        return [person for person in self.people if person.email == email]
    
    def get_group_members(self, group_number):
        return [person for person in self.people if person.group_number == group_number]

    def get_groupless_students(self):
        return [person for person in self.people if not person.is_teacher and not person.group_number]
