'''Модуль с декоратором который позволяет выполнить функцию n раз'''
import functools
def repeat_decorator(times = 2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for i in range(times):
                result = func(*args, **kwargs)
                print(func.__name__)
            return result
        return wrapper
    return decorator

