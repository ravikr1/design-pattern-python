from interface_car import ICar

class HybridCar(ICar):

    def __init__(self):
        self._height = 15
        self._width = 33
        self._length = 44
        self.wheelbase = 3200


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
        return "The price range is from 12-46L"