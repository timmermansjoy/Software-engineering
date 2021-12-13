from IPrintable import IPrintable
import abc

class Print_strategy(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass
    def print_person(self, IPrintable):
        pass