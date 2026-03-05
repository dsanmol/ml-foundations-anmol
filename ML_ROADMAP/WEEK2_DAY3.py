#ENUM
from enum import Enum
class Color(Enum):
    RED=1
    GREEN=2
    BLUE=3
print(Color)
print((Color.RED))
print((Color.RED.name))
print((Color.RED.value))    

a:int            #this is called type hinting here we are telling the compiler that a is of type int but we are not assigning any value to it and its 
a=10
print(a)
print(type(a))
a="hello"
print(a)
print(type(a))
kwg={"a":"john","b":20}
def fun(a:str,b:int):
    print(a)
    print(b)

fun(**kwg)
class anima:
    clsvar="janwar"
    def __init__(self,name:str,age:int):
        self.name=name
        self.age=age
ob=anima("dog",5)
print(ob.name)
print(ob.age)
print(ob.clsvar)
ob.clsvar="pashu"
print(ob.clsvar)
ob2=anima("cat",3)
print(ob2.clsvar)                            #here this class variable didnt change it remains same as defined under class anima
class prac:
    def __init__(self,name,age,**kwargs):
        self.name=name
        self.age=age
        self.kwargs=kwargs
    def display(self,place)->None:
        print(self.name)
        print(self.age)
        print(place)
        print(self.kwargs)
        

kwargs={"name":"john","age":20}
ob=prac(**kwargs,country="india",state="delhi")
a=ob.display("dELHI")     
dc=dict[str,int]
dc.update({1:"ac",2:"bc"})
print(dc)