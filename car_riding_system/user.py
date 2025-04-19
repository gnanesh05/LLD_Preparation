class User:
    def __init__(self, name):
        self.name = name

class Customer(User):
    def __init__(self,name):
        super().__init__(name)


class Driver(User):
    def __init__(self,name):
        super().__init__(name)