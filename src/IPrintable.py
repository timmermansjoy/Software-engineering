import abc
class IPrintable(abc.ABC):
    @abc.abstractmethod
    def __init__(self, given_name, surname):
        pass