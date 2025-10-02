A Python decorator is a special function that modifies the behavior of another function or method. Decorators are often used to add functionality (such as logging, timing, or access control) to existing functions without changing their code. They are applied using the @decorator_name syntax above the function definition.

def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function runs
# Hello!
# After function runs