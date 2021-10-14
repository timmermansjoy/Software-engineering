import pytest

import src as program


@pytest.fixture()
def seut():
    seut = program.Student(0, "m", "firstname", "lastname", "f.n@mail.com", "test12345")
    yield seut


class TestResource:
    def test_freshStudentNoGroupnumber(self, seut):
        assert seut.group_number is None

    def test_studentWithGroupHasGroupNumber(self, seut):
        group_size = 1
        student_list = [seut]
        program.make_group(student_list, group_size, 1)
        assert seut.group_number == 1
