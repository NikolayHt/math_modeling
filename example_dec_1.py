# Можем передать название файла, 
# куда будет происходить запись результата суммы

def logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as f:
                f.write(str(result))
            return result
        return wrapped
    return decorator

# Декоратор logger должен принимать имя файла и возвращать декоратор, 
# который принимает функцию и подменяет её функцией wrapped

@logger('file_log.txt')
def summator(list_of_num):
    return sum(list_of_num)

summator([1,2,3,4])