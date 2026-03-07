#decorator


def dec(func):

    def inner():
        print("Function ke pehle")
        func()
        print("Function ke baad")
    return inner

@dec                                                     # this is equal to ->hello=dec(hell0)
def hello():                                             
    print("Hello Bhaiji")


hello()

#Route Register
class App():
    def __init__(self):
        self.routes={}

    def add_routes(self,path,func):
        self.routes[path]=func

    def route(self,path):
        def dec(func):
            self.add_routes(path,func)
            return func        
        return dec
    
app=App()
@app.route("/greet")
def grt():
    print("Hello Bhaisaab")
grt()
print(app.routes)