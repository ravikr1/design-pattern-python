# pylint: disable=too-few-public-methods
"The Car Interface"
from abc import ABCMeta, abstractmethod

class ICar(metaclass=ABCMeta):
    "The Car Interface (Product)"

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "A static interface method"

    @staticmethod
    @abstractmethod
    def get_price_range():
        "A static interface method"