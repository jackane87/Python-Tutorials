from functools import wraps
from time import sleep

def delay(t):
    def inner(fn):
        def wrapper(*args, **kwargs):
            print(f'Waiting {t}s before running {fn.__name__}')
            sleep(t)
            return fn(*args, **kwargs)
        return wrapper
    return inner

@delay(3)
def say_hi():
    return "hi"

print(say_hi())