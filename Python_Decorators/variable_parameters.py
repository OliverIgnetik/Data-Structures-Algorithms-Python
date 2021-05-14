def mul_decorator(func):
    def wrapper(*args, **kwargs):
        print('function', func.__name__, 'called with args - ',
              args, 'and kwargs - ', kwargs)
        result = func(*args, **kwargs)
        print('function', func.__name__, 'returns', result)
        return result
    return wrapper


@mul_decorator
def mul(a, b):
    return a * b


mul(3, 3)
mul(3, b=6)
