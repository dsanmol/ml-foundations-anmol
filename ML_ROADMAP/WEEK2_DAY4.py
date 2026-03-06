class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
ob=animal("dog","mammal")
print(getattr(ob,"abc",None))

class excp(Exception):
    def __init__(self, b):
        self.b = b
        super().__init__(b)

b = 0

try:
    if b == 0:
        raise excp(b)

except excp as e:
    print("Exception handled Saale zero se kyu divide karna hai tereko:", e.b)           
    
        
