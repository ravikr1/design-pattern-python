from abc import ABCMeta, abstractmethod

class ICar(metaclass=ABCMeta):
    "The Car Interface (Product)"

    @staticmethod
    @abstractmethod
    def get_price():
        "A static interface method"

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "A static interface method"