from src.Student import Student
from src.teacher import Teacher
from src.EmailParser import EmailParser


class PersonFactory:
    def create_person(self, number, gender, given_name, surname, email, GUID, group_number):
        if EmailParser.is_student(email):
            return Student(number, gender, given_name, surname, email, GUID, group_number)
        if EmailParser.is_teacher(email):
            return Teacher(number, gender, given_name, surname, email, GUID, group_number)
        raise Exception("Unknown type")
