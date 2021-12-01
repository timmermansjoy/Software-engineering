from student import Student
from teacher import Teacher

class PersonFactory():
    
    def create_person(self, type, number, gender, given_name, surname, email, GUID):
        if type == 'STUDENT':
            return Student(number, gender, given_name, surname, email, GUID)
        elif type == 'TEACHER':
            return Teacher(number, gender, given_name, surname, email, GUID)
        else:
            raise Exception('Unknown type')