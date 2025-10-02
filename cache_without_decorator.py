import functools

def fibonacci(n, cahce={}):
    if n in cahce:
        return cahce[n]
    if n <= 2:
        return n
    else:
        result = fibonacci(n-1, cahce) + fibonacci(n-2, cahce)
        cahce[n] = result
        return result
    
print(fibonacci(40))  # Output: 55