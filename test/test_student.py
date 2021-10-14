import pytest

from src.student import Student
from src.helpers import Helper


@pytest.fixture()
def sut():
    sut = Student(0, "m", "firstname", "lastname", "f.n@mail.com", "test12345")
    yield sut


class TestResource:
    def test_freshStudentNoGroupnumber(self, sut):
        assert sut.group_number is None

    def test_studentWithGroupHasGroupNumber(self, sut):
        group_size = 1
        student_list = [sut]
        helper = src.Helper()
        helper.setHelperStudents(student_list)
        helper.make_group(student_list, group_size, 1)
        assert sut.group_number == 1

    def test_studentInfoOutput(self, sut):
        infoOutput = sut.info()
        assert infoOutput == "0 firstname lastname \t f.n@mail.com \t m"

    def test_name_print(self, sut):
        simple_print = sut.name_print()
        assert simple_print == "firstname lastname"
