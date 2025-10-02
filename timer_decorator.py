import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__!r} took {end_time - start_time:.4f} seconds to run.")
        return result
    return wrapper

@timer
def calculate_sum(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum




a=calculate_sum(100000)
print(a)