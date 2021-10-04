import pytest
from src import student
from src.group import Group
from src.student import Student
from src.helpers import Helper

@pytest.fixture()
def sut():
    sut0 = Student(0, "m", "firstname", "lastname", "f.n@mail.com", "test12345")
    sut1 = Student(1, "m", "firstname1", "lastname1", "f1.n1@mail1.com1", "test1")
    sut2 = Student(2, "f", "firstname2", "lastname2", "f2.n1@mail1.com1", "test2")
    sut3 = Student(3, "m", "firstname3", "lastname3", "f3.n1@mail1.com1", "test3")
    sut = [sut0, sut1, sut2, sut3]
    yield sut

class TestResource:
    def test_make_group(self, sut):
        helper = Helper()
        helper.setHelperStudents(sut)
        thisGroup = helper.make_group(sut, 4, 1)
        for student in sut:
            assert student.group_number == 1
        
    def test_print_students(self, sut):
        helper = Helper()
        helper.setHelperStudents(sut)
        assert helper.print_students() == "firstname lastname firstname1 lastname1 firstname2 lastname2 firstname3 lastname3"