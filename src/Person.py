# from abc import ABC
# from abc import abstractmethod
# from abc import ABCMeta
from IPrintable import IPrintable
import abc

class Person(IPrintable):
    @abc.abstractmethod
    def __str__(self):
        raise NotImplementedError

    @abc.abstractmethod
    def __repr__(self):
        raise NotImplementedError

    @abc.abstractmethod
    def info(self):
        raise NotImplementedError

    @abc.abstractmethod
    def name_print(self):
        raise NotImplementedError
