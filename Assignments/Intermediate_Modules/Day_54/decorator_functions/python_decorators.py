# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2


# def multiply(n1,n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# # Functions are first-class objects.  The can be passed aroung as arguments e.g. int/str/float etc.
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
#
# result = calculate(add, 2, 3)
# # print(result)
#
# # Nested functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#
#
# # Functions can be returned from other functions
# inner_function = outer_function()
# inner_function()


""" Python decorator functions"""
import time

def delay_decorator(function):
    def wrapper_function():
        # Do something before the function
        time.sleep(2)
        function()
        function()
    # Do something after the function
    return wrapper_function


"""
Decorator function - a function which wraps another function 
and gives it some additional functionality or modifies its functionality;
aka 'syntactic sugar'
"""
@delay_decorator
def say_deez_nuts():
    print("Carpe deez nuts!")


@delay_decorator
def say_git_sum():
    print("Get after it, Bitches!")


def say_sup():
    print("Wasssssuuuuuup?!")



decorated_function = delay_decorator(say_sup)
decorated_function()

