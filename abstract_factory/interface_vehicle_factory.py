from abc import ABCMeta, abstractmethod

class IVehicleFactory(metaclass=ABCMeta):
    #Abstract vehicle factory interface

    @staticmethod
    @abstractmethod
    def get_price(vehicle):
        "The static Abstract factory interface method"