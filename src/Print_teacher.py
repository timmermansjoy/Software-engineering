from src.Print_strategy import Print_strategy


class Print_teacher(Print_strategy):
    def __init__(self):
        pass

    def print_person(self, IPrintable):
        return "{} {} {}".format(IPrintable.given_name, IPrintable.surname, "TEACHER")
