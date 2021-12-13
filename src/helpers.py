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
        if 'group_number' not in person_data:
            person_data["group_number"] = 0
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
                    group_number=row['group_number']
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
                    group_number=row['group_number']
                )
                print("Teacher found!")
                self.people.append(person)
            else:
                raise Exception("Invalid email???? :(((")
        person_data.to_csv(f"./data/{filename}", index=False)
        return self.people

    def make_group(self, students_in_group, group_number, teacher):
        filename = teacher.split("@")[0].strip(".") + ".csv"
        person_data = pd.read_csv(f"./data/{filename}")
        group = Group(students_in_group, group_number)
        for student in students_in_group:
            student.add_to_group(group_number)
            student_index = student.number -1
            person_data.at[student_index, 'group_number'] = int(group_number)
            # person_data["group_number"][student.number] = student.group_number
            # person_data.replace({'group_number': {student.number: student.group_number}}, inplace=True)
        person_data.to_csv(f"./data/{filename}", index=False)
        return group

    def print_people(self):
        for person in self.people:
            x = person.name_print()
            print(x)
            
    def get_next_group_number(self):
        group_numbers = [person.group_number for person in self.people if person.group_number is not None]
        if group_numbers:
            return max(group_numbers) + 1
        else:
            return 1

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
