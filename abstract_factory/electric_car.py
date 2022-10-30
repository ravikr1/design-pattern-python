from interface_car import ICar

class ElectricCar(ICar):

    def __init__(self):
        self._height = 14
        self._width = 32
        self._length = 43
        self._wheelbase = 3200


    def get_dimensions(self):
        """ Returns the dimensions of the Car"""
        return {
            "width": self._width,
            "length": self._length,
            "height": self._height,
            "wheelbase" : self._wheelbase
        }

    def get_price_range(self):
        """ Returns the price range of the Car"""
        return "The price range is from 9-40L"