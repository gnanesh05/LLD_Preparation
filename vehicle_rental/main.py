from Car import Car
from Bike import Bike

car = Car("BMW",100)
bike = Bike("pulsar", 20)

print(car.get_type(), car.calculate_rental(2))
print(bike.get_type(), bike.calculate_rental(1))
