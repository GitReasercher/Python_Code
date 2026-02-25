import time
from unittest import result


def decorator(countdown):
    def wrapper():
        print("3...2...1...")
        countdown()
    return wrapper


@decorator
def boom():
    time.sleep(3)
    print('Boom!')

boom()


