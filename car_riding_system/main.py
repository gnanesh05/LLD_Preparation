from ride_service import RidingService
from user import Customer, Driver


customer1 = Customer("jake")
driver1 = Driver("peralta")

ride_service = RidingService()

ride1 = ride_service.assign_ride(customer1, driver1,"home","office")
ride_service.start_ride(ride1)
ride_service.end_ride(ride1)
print(ride1)