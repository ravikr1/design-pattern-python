# pylint: disable=too-few-public-methods
"Abstract Vehicle Factory"
from interface_vehicle_factory import IVehicleFactory
from car_factory import CarFactory
from bus_factory import BusFactory

class VehicleFactory(IVehicleFactory):
    "The Abstract Factory Concrete Class"

    @staticmethod
    def get_vehicle(vehicle):
        "Static get_factory method"
        try:
            if vehicle.lower() in ['electriccar', 'hybridcar', 'petrolcar']:
                return CarFactory.get_car(vehicle)
            if vehicle.lower() in ['electricbus', 'hybridbus', 'petrolbus']:
                return BusFactory.get_bus(vehicle)
            raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None