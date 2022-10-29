"The Factory Class"

from hatchback import HatchBack
from sedan import Sedan
from suv import SUV

class CarFactory:
    "The Factory Class"

    @staticmethod
    def get_car(car):
        "A static method to get a chair"
        if car.lower() == 'hatchback':
            return HatchBack()
        if car.lower() == 'sedan':
            return Sedan()
        if car.lower() == 'suv':
            return SUV()
        return None