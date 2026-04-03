def hello_world():
    print("Привет")

hello_world()

import time

def check_time(func):
    def wrapper(*args, **kwargs):
        '''наш декоратор - подсчет выполнения скорости работы'''
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Функция {func} отработала за {end-start:.10f} секунд")

        return
    return wrapper
@check_time
def lazy_func():
    print("Я ленивый капец")
    #time.sleep(5)
    print("Наконец-то я поднялся с кровати")

lazy_func()