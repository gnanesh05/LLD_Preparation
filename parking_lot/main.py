from Parking import ParkingLevel, ParkingLot, ParkingSpot
from Vehicle import Bike, Car, Truck
# Create some parking spots
spots_level_0 = [ParkingSpot(1,"small"), ParkingSpot(2,"medium"), ParkingSpot(3,"large")]
spots_level_1 = [ParkingSpot(4,"medium"), ParkingSpot(5,"large")]

# Create levels
level0 = ParkingLevel(0, spots_level_0)
level1 = ParkingLevel(1, spots_level_1)

# Create parking lot
parking_lot = ParkingLot([level0, level1])

# Park vehicles
bike = Bike("BIKE123")
car = Car("CAR456")
truck = Truck("TRUCK789")

parking_lot.park_vehicle(bike)
parking_lot.park_vehicle(car)
parking_lot.park_vehicle(truck)
