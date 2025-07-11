from threading import Thread
from elevator import Elevator
from request import Request

class ElevatorSystem:
    def __init__(self, num_of_elevators, capacity):
        self.elevators = []
        self.threads = []
        try:
            for i in range(num_of_elevators):
                elevator = Elevator(i+1,capacity)
                self.elevators.append(elevator)
                t = Thread(target=elevator.run)
                t.start()
                self.threads.append(t)
        except Exception as e:
            print(e)
            self.stop_all()



    def find_optimal_elevator(self, source_floor:int, destination_floor:int)->Elevator:
        optimal_elevator = None
        min_distance = float('inf')
        for elevator in self.elevators:
            diff = abs(source_floor - elevator.current_floor)
            if diff < min_distance:
                min_distance = diff
                optimal_elevator = elevator
        return optimal_elevator

    def request_elevator(self, source_floor:int, destination_floor:int):
        optimal_elevator = self.find_optimal_elevator(source_floor, destination_floor)
        optimal_elevator.add_request(Request(source_floor, destination_floor))

    def stop_all(self):
        for elevator in self.elevators:
            elevator.stop()
        for thread in self.threads:
            thread.join()
        print("Stopping all processes")