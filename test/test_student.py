from attr import Factory
import pytest
import src
from src.CsvReader import CsvReader
from src.CsvWriter import CsvWriter
from src.GroupFactory import GroupFactory
from src.Populator import Populator

@pytest.fixture()
def sut():
    sut = src.Student(1, "m", "firstname", "lastname", "f.n@student.pxl.be", "test12345", 0)
    yield sut


class TestResource:
    def test_freshStudentNoGroupnumber(self, sut):
        assert sut.group_number is 0

    def test_studentWithGroupHasGroupNumber(self, sut):
        backup = CsvReader.read_file('test.csv')
        student_list = [sut]
        populator = Populator()
        populator.populate_people('test.csv')
        factory = GroupFactory(populator)
        GroupFactory.create_group(factory, student_list, 'test.csv' )
        CsvWriter.write_file(backup, 'test.csv')
        assert sut.group_number == 1

    def test_studentInfoOutput(self, sut):
        infoOutput = sut.info()
        assert infoOutput == "1 firstname lastname \t f.n@student.pxl.be \t m"

    def test_name_print(self, sut):
        simple_print = sut.name_print()
        assert simple_print == "firstname lastname"
