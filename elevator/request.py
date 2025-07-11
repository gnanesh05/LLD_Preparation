from direction import Direction
class Request:
    def __init__(self,current_floor, destination_floor):
        self.current_floor = current_floor
        self.destination_floor = destination_floor
        self.direction = Direction.UP if current_floor < destination_floor else Direction.DOWN