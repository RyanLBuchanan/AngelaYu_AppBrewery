import time
current_time = time.time()
print(f"Current time: {current_time} seconds.")

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__.title()} run speed: {end_time - start_time} seconds.")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()