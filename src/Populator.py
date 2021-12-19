from src.CsvReader import CsvReader
from src.CsvWriter import CsvWriter
from src.PersonFactory import PersonFactory
from src.EmailParser import EmailParser


class Populator:
    def __init__(self):
        self.person_factory = PersonFactory()
        self.people = []

    def populate_people(self, filename):
        data = CsvReader.read_file(filename)
        if self.people:
            return self.people
        try:
            for _, row in data.iterrows():
                person = self.person_factory.create_person(
                    number=row["Number"],
                    given_name=row["GivenName"],
                    surname=row["Surname"],
                    email=row["EmailAddress"],
                    gender=row["Gender"],
                    GUID=row["GUID"],
                    group_number=row["group_number"],
                )
                self.people.append(person)
            CsvWriter.write_file(data, filename)
        except Exception as e:
            raise Exception(e.message)
        return self.people
