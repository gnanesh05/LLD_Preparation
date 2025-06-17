from Vehicle import Vehicle
from typing import List

class ParkingSpot:
    def __init__(self, number,size):
        self.number = number
        self.size = size
        self.vehicle : Vehicle = None

    def __canFit(self,vehicle:Vehicle):
            size_order = {"small": 1, "medium": 2, "large": 3}
            return self.vehicle is None and size_order[self.size] >= size_order[vehicle.get_spot_size()]
    
    def park(self, vehicle:Vehicle):
         if self.__canFit(vehicle):
              self.vehicle = vehicle
              return True
         return False
    
    def leave(self):
        self.vehicle = None


class ParkingLevel:
    def __init__(self,level_number,spots: List[ParkingSpot]):
        self.level_number = level_number
        self.spots = spots
    
    def park_vehicle(self, vehicle:Vehicle):
        for spot in self.spots:
            if spot.park(vehicle):
                print(f"Vehicle {vehicle.plate_number} parked at level {self.level_number}, spot {spot.number}")
                return True
        print(f"No available spot for {vehicle.plate_number} at level {self.level_number}")
        return False
    
    def unpark_vehicle(self,spot_number):
         for spot in self.spots:
            if spot.number == spot_number:
                spot.leave()
                print(f"Spot {spot_number} at level {self.level_number} is now free.")
                return


class ParkingLot:
    def __init__(self, levels: List[ParkingLevel]):
        self.levels = levels

    def park_vehicle(self, vehicle:Vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False
    
    def unpark_vehicle(self, vehicle):
        for level in self.levels:
            level.unpark_vehicle(vehicle)
            return True
        return False
    
    



    
          
          
