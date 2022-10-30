"Abstract Factory Use Case Example Code"

from vehicle_factory import VehicleFactory

Vehicle1 = VehicleFactory.get_vehicle("electriccar")
print(f"{Vehicle1.__class__} : {Vehicle1.get_dimensions()}")
print(Vehicle1.get_price_range())
print(" ============================================================== ")

Vehicle2 = VehicleFactory.get_vehicle("hybridbus")
print(f"{Vehicle2.__class__} : {Vehicle2.get_dimensions()}")
print(Vehicle2.get_price_range())