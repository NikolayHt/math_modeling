def decorator(func):
    def wrapper_function(*args, **kwargs):
        #print(*args, **kwargs)
        func(*args, **kwargs)
        print(*args, **kwargs)
    return wrapper_function


@decorator
def greet(name, v = 10):
    print(f"Привет {name}! {v}")

greet("Анастасия")