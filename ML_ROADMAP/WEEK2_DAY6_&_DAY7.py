# Revesion + Practice of Python fundamentals
class shape:
    def __init__(self,name,sides):
        self.name=name
        self.sides=sides
    def data(self)->None:
        print(f"{self.name} has {self.sides} sides.")

class square(shape):
    def __init__(self,side)->None:
        super().__init__("Square",4)
        self.side=side
    def area(self)->int:
        return self.side * self.side
    
ob=square(4)
print(ob.area())    
#print(ob.data())                # here this will return none as we print it so we will not print when our fucn return None
ob.data()

def calci(add):
    def inner(a,b):
        c=add(a,b)
        print(f"Ye raha sum:{c}")
    return inner  
  
@calci
def addi(a,b):
    return a+b

addi(2,3)

def calci1(a,b):
    return add1(a,b)

def add1(a,b):
    return a+b

print(calci1(2,3))