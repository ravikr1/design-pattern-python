"The Factory Class"

from electric_bus import ElectricBus
from petrol_bus import PetrolBus
from hybrid_bus import HybridBus

class BusFactory:  # pylint: disable=too-few-public-methods
    "The Factory Class"

    @staticmethod
    def get_bus(bus):
        "A static method to get a bus"
        try:
            if bus.lower() == 'electricbus':
                return ElectricBus()
            if bus.lower() == 'hybridbus':
                return HybridBus()
            if bus.lower() == 'petrolbus':
                return PetrolBus()
            raise Exception('Chair Not Found')
        except Exception as _e:
            print(_e)
        return None