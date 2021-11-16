import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def meyada_function():
        first_time = time.time()
        local_time = time.ctime(first_time)
        function()
        endtime= time.time()
        print(f"Local Time: {local_time}\n\n{function.__name__} run speed: {endtime - first_time} second")
    return meyada_function

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