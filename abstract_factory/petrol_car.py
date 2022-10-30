from interface_car import ICar

class PetrolCar(ICar):

    def __init__(self):
        self._height = 14
        self._width = 30
        self._length = 42
        self.wheelbase = 3150


    def get_dimensions(self):
        """ Returns the dimensions of the Car"""
        return {
            "width": self._width,
            "length": self._length,
            "height": self._height,
            "wheelbase" : self.wheelbase
        }

    def get_price_range(self):
        """ Returns the price range of the Car"""
        return "The price range is from 10-56L"