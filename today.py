from main import check_time, hello_world

from repeat import repeat_decorator
@repeat_decorator(times=2)
def perebor():
    nums = range(1, 5)
    for i in nums:
        i= i **2
        print(i)
print(perebor.__name__)