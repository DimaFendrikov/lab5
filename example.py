from functools import wraps

# Декоратор кешування
def my_cache(func):
    cache = {}

    @wraps(func)
    def new_function(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        
        if key in cache:
            print("Дані з кешу:")
            return cache[key]
        
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return new_function

@my_cache
def multiply(a, b):
    return a * b

@my_cache
def string(*strings):
    return ' '.join(strings)

@my_cache
def sum(a, b, c=0):
    return a + b + c

print(multiply(5, 6))  # Обчислюється результат
print(multiply(5, 6))  # Витягується з кешу

print(string("hello", "world"))  
print(string("hello", "world")) 

print(sum(1, 2)) 
print(sum(1, 2, 3))
print(sum(1, 2))