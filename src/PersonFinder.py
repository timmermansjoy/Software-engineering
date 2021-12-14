from Populator import Populator


class PersonFinder:
    def __init__(self, populator=None):
        self.populator = populator if populator is not None else Populator()

    def get_person_by_email(self, filename, email):
        people = self.populator.populate_people(filename)
        person = [person for person in people if person.email == email]
        return person[0]

    def print_people(self, filename):
        people = self.populator.populate_people(filename)
        for person in people:
            print(person.print_strategy.print_person(person))
