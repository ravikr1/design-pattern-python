# pylint: disable=too-few-public-methods
"The Bus Interface"
from abc import ABCMeta, abstractmethod

class IBus(metaclass=ABCMeta):
    "The Bus Interface (Product)"

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "A static interface method"

    @staticmethod
    @abstractmethod
    def get_price_range():
        "A static interface method"