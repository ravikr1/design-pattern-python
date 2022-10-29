from interface_car import ICar

class Sedan(ICar):
    "The Sedan Concrete Class implements the ICar interface"

    def __init__(self):
        self._height = 68
        self._width = 72
        self._length = 186
        self._wheelbase = 102

    def get_dimensions(self):
        return {
            "width": self._width,
            "length": self._length,
            "height": self._height,
            "wheelbase": self._wheelbase
        }

    def get_price(self):
        return "The average price range is around 16L"