"""Keyword Arguments"""


def my_function(a, b, c):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    pass


# my_function(a=1, b=2, c=3)

"""Arguments with Default Values"""


def my_function_default(a=1, b=2, c=3):
    # Do this with a
    print(a)
    # Then do this with b
    print(b)
    # Finally do this with c
    print(c)


# my_function_default(b=5)

"""Unlimited Positional Arguments"""
def my_add(*args):
    print(args)
    my_sum = 0
    for n in args:
        my_sum += n
    return my_sum


# print(my_add(1, 2, 3, 4, 5, 6, 7, 8))

def my_calculate(n, **kwargs):
    # print(type(kwargs))
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


my_calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")

# my_car = Car(make="Delorean", model="DMC-12")
my_car = Car(model="DMC-12")
print(my_car.make)
