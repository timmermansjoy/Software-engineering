import pytest
import src

@pytest.fixture()
def sut():
    sut0 = src.Student(0, "m", "firstname", "lastname", "f.n@mail.com", "test12345")
    sut1 = src.Student(1, "m", "firstname1", "lastname1", "f1.n1@mail1.com1", "test1")
    sut2 = src.Student(2, "f", "firstname2", "lastname2", "f2.n1@mail1.com1", "test2")
    sut3 = src.Student(3, "m", "firstname3", "lastname3", "f3.n1@mail1.com1", "test3")
    sut = [sut0, sut1, sut2, sut3]
    yield sut

class TestResource:
    def test_make_group(self, sut):
        helper = src.Helper()
        helper.setHelperStudents(sut)
        thisGroup = helper.make_group(sut, 4, 1)
        for student in sut:
            assert student.group_number == 1

def test_print_students(capfd):
    sut0 = src.Student(0, "m", "firstname", "lastname", "f.n@mail.com", "test12345")
    sut1 = src.Student(1, "m", "firstname1", "lastname1", "f1.n1@mail1.com1", "test1")
    sut2 = src.Student(2, "f", "firstname2", "lastname2", "f2.n1@mail1.com1", "test2")
    sut3 = src.Student(3, "m", "firstname3", "lastname3", "f3.n1@mail1.com1", "test3")
    sut = [sut0, sut1, sut2, sut3]
    helper = src.Helper()
    helper.setHelperStudents(sut)
    helper.print_students()
    out, err = capfd.readouterr()
    assert  out== "firstname lastname\nfirstname1 lastname1\nfirstname2 lastname2\nfirstname3 lastname3\n"
