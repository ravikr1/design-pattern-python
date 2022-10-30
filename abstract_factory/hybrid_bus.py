from interface_bus import IBus

class HybridBus(IBus):

    def __init__(self):
        self._height = 23
        self._width = 54
        self._length = 82
        self.wheelbase = 6100


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
        return "The price range is from 28-70L"