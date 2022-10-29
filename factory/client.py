"Factory Use Case Example Code"

from car_factory import CarFactory

# The Client
print("First type")
Car = CarFactory.get_car("hatchback")
print(Car.get_dimensions())
print(Car.get_price())
print("==============================\n")
print("Second type")
Car = CarFactory.get_car("suv")
print(Car.get_dimensions())
print(Car.get_price())
print("==============================\n")
print("third type")
Car = CarFactory.get_car("sedan")
print(Car.get_dimensions())
print(Car.get_price())