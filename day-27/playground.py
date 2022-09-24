def add(*args):
    sum_final = sum(args)
    return sum_final


print(add(46, 25, 61, 87, 26))

def calculate(n, **kwargs):
    print(kwargs)
    # for (key, value) in kwargs.items:
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make)
        self.model = kw.get("model")
        self.color =  kw.get("color")

my_car = Car(make="Nissan", model="GTR")
print(my_car.model)