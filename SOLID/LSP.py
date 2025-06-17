from abc import ABC, abstractmethod
class Bird:
    def fly(self):
        print("This bird can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich is flying")


#problem here is that we say all birds can fly but clearly we know ostrict can't
#when we create an Ostrich class that inherits from Bird and overrides fly(), it violates the Liskov Substitution Principle (LSP)

class Bird1(ABC):
    def __init__(self,name):
        self.name = name

class FlyingBird(Bird1):
    @abstractmethod
    def fly(self):
        pass

class Sparrow1(FlyingBird):
    def fly(self):
        return f'{self.name} is flying'
    
class Ostrict1(Bird1):
    def walk(self):
        return f'{self.name} is walking'


ost = Ostrict1('osty')
print(ost.walk())