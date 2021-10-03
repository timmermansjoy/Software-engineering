import pytest

from student import Student
from main import make_group


@pytest.fixture()
def seut():
    seut = Student(0, "m", "firstname", "lastname", "f.n@mail.com", "test12345")
    yield seut

class TestResource:
    def test_freshStudentNoGroupnumber(self, seut):
        assert seut.group_number == None

    def test_studentWithGroupHasGroupNumber(self, seut):
        group_size = 1
        student_list = [seut]
        make_group(student_list, group_size, 1)
        assert seut.group_number == 1
