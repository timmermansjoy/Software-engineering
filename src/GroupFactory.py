from src.group import Group
from src.Populator import Populator
from src.CsvReader import CsvReader
from src.CsvWriter import CsvWriter


class GroupFactory:
    def __init__(self, populator=None):
        self.populator = populator if populator is not None else Populator()

    def create_group(self, members, filename):
        if not self.is_valid_group:
            raise Exception("Invalid group members")
        group_number = self.get_next_group_number(filename)
        group = Group(members, group_number)

        data = CsvReader.read_file(filename)
        for student in members:
            student.add_to_group(group_number)
            student_index = student.number - 1
            data.at[student_index, "group_number"] = int(group_number)
        CsvWriter.write_file(data, filename)
        return group

    def get_group_members(self, group_number, filename):
        people = self.populator.populate_people(filename)
        return [person for person in people if person.group_number == group_number]

    def get_next_group_number(self, filename):
        people = self.populator.populate_people(filename)
        return max([person.group_number for person in people]) + 1

    def is_valid_group(self, members):
        uniques = []
        for member in members:
            if member in uniques or member == "Select...":
                return False
            uniques.append(member)
        return True
