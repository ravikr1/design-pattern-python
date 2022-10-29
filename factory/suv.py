from interface_car import ICar

class SUV(ICar):
    "The Suv Concrete Class implements the ICar interface"

    def __init__(self):
        self._height = 76
        self._width = 78
        self._length = 196
        self._wheelbase = 112

    def get_dimensions(self):
        return {
            "width": self._width,
            "length": self._length,
            "height": self._height,
            "wheelbase": self._wheelbase
        }

    def get_price(self):
        return "The average price range is around 15L"