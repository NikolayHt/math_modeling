def Calc(num):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, num)
            print(result)
            return result
        return wrapped
    return decorator

@Calc(11)
def summator(a, b = 22):
    return a + b

summator()