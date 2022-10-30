"The Factory Class"

from electric_car import ElectricCar
from petrol_car import PetrolCar
from hybrid_car import HybridCar

class CarFactory:  # pylint: disable=too-few-public-methods
    "The Factory Class"

    @staticmethod
    def get_car(car):
        "A static method to get a car"
        try:
            if car.lower() == 'electriccar':
                return ElectricCar()
            if car.lower() == 'hybridcar':
                return HybridCar()
            if car.lower() == 'petrolcar':
                return PetrolCar()
            raise Exception('Chair Not Found')
        except Exception as _e:
            print(_e)
        return None