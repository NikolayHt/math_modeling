# *args - произвольное число позиционных аргументов.  
# При вызове функции, на место этого 
# параметра передается список аргументов, заключенных в кортеж
# **kwargs - произвольное число именованных аргументов. При вызове функции, 
# на его место передается список именованных аргументов заключенных в словарь, 
# кроме тех, имена которых были определены ранее

def decorator(func):
    def wrapper_function(*args, **kwargs):
        #print(*args, **kwargs)
        func(*args, **kwargs)
        print(*args, **kwargs)
    return wrapper_function


@decorator
def greet(name):
    print(f"Привет {name}!")

greet("Анастасия")