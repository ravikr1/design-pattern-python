from interface_bus import IBus

class PetrolBus(IBus):

    def __init__(self):
        self._height = 21
        self._width = 51
        self._length = 70
        self.wheelbase = 6150


    def get_dimensions(self):
        """ Returns the dimensions of the Bus"""
        return {
            "width": self._width,
            "length": self._length,
            "height": self._height,
            "wheelbase" : self.wheelbase
        }

    def get_price_range(self):
        """ Returns the price range of the Bus"""
        return "The price range is from 22-60L"