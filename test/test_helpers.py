import pytest
import src
from src.CsvReader import CsvReader
from src.CsvWriter import CsvWriter
from src.GroupFactory import GroupFactory
from src.PersonFinder import PersonFinder
from src.Populator import Populator


@pytest.fixture()
def sut():
    sut0 = src.Student(1, "m", "firstname", "lastname", "f.n@mail.com", "test12345",0)
    sut1 = src.Student(2, "m", "firstname1", "lastname1", "f.n1@student.pxl.be", "test1",0)
    sut2 = src.Student(3, "f", "firstname2", "lastname2", "f.n2@student.pxl.be", "test2",0)
    sut3 = src.Student(4, "m", "firstname3", "lastname3", "f.n3@student.pxl.be", "test3",0)
    sut = [sut0, sut1, sut2, sut3]
    yield sut


class TestResource:
    def test_make_group(self, sut):
        backup = CsvReader.read_file('test.csv')
        student_list = sut
        populator = Populator()
        populator.populate_people('test.csv')
        factory = GroupFactory(populator)
        GroupFactory.create_group(factory, student_list, 'test.csv')
        CsvWriter.write_file(backup, 'test.csv')
        for student in sut:
            assert student.group_number == 1


def test_print_students(capfd):
    sut0 = src.Student(1, "m", "firstname", "lastname", "f.n@mail.com", "test12345",0)
    sut1 = src.Student(2, "m", "firstname1", "lastname1", "f.n1@student.pxl.be", "test1",0)
    sut2 = src.Student(3, "f", "firstname2", "lastname2", "f.n2@student.pxl.be", "test2",0)
    sut3 = src.Student(4, "m", "firstname3", "lastname3", "f.n3@student.pxl.be", "test3",0)
    sut = [sut0, sut1, sut2, sut3]
    backup = CsvReader.read_file('test.csv')
    student_list = sut
    populator = Populator()
    populator.populate_people('test.csv')
    personfinder = PersonFinder(populator)
    personfinder.print_people('test.csv')
    out, err = capfd.readouterr()
    CsvWriter.write_file(backup, 'test.csv')
    assert out == "firstname lastname STUDENT\nfirstname1 lastname1 STUDENT\nfirstname2 lastname2 STUDENT\nfirstname3 lastname3 STUDENT\nJoffrey Blaak TEACHER\n"
