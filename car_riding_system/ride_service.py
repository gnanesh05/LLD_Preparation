class Ride:
    def __init__(self,customer, driver,pickup, drop,status):
        self.customer = customer
        self.driver = driver
        self.pickup = pickup
        self.drop = drop
        self.status = status

    def get_status(self):
        print(self.status)

    def set_status(self, status):
        self.status = status
        self.get_status()

    def __str__(self):
        return f"Ride({self.customer.name} -> {self.drop}, Status: {self.status})"



class RidingService:
    def assign_ride(self,customer, driver, pickup, drop):
        return Ride(customer, driver, pickup, drop, status="NEW")
    def start_ride(self, ride:Ride):
        ride.set_status("start")

    def end_ride(self, ride:Ride):
        ride.set_status("end")
    def cancel_ride(self,ride:Ride):
        ride.set_status("cancel")
