import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper

def calculate_sum(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

calculate_sum=timer(calculate_sum)



a=calculate_sum(100000)
print(a)