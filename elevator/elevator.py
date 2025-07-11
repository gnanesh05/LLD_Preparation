from threading import Lock,Condition
from direction import Direction
from request import Request
from collections import deque
import time

class Elevator:
    def __init__(self,id:int, capacity:int):
        self.id = id
        self.capacity = capacity
        self.current_floor = 0
        self.direction = Direction.UP
        self.requests = deque()
        self.lock = Lock()
        self.condition = Condition(self.lock)
        self.isRunning = True

    def add_request(self, request:Request):
        with self.lock:
            if len(self.requests) < self.capacity:
                self.requests.append(request)
                print(f"Elevator {self.id} added request from {request.current_floor} floor to {request.destination_floor} floor")
                self.condition.notify_all()
    
    def get_next_request(self)->Request:
        with self.lock:
            while not self.requests:
                self.condition.wait()
            return self.requests.popleft()
    
    def process_request(self, request:Request):
        start_floor = self.current_floor
        end_floor = request.destination_floor

        if start_floor < end_floor:
            self.direction = Direction.UP
            for i in range(start_floor, end_floor+1):
                self.current_floor = i
                print(f"Elevator {self.id} reached {i} floor")
                time.sleep(1)
        elif start_floor > end_floor:
            self.direction = Direction.DOWN
            for i in range(start_floor, end_floor-1, -1):
                self.current_floor = i
                print(f"Elevator {self.id} reached {i} floor")
                time.sleep(1)

    def process_requests(self):
        while True:
            request = self.get_next_request()
            self.process_request(request)

    def run(self):
        while self.isRunning:
            self.process_requests()

    def stop(self):
        self.isRunning = False