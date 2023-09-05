def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n-1)

def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

def recursive_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
        
print(recursive_sum(4))
print(recursive_factorial(3))
print(recursive_fibonacci(5))

def add_n_to_value(n):
    def inner_function(value):
        return value + n
    return inner_function

add_5 = add_n_to_value(5)
result = add_5(10)
print(result)
