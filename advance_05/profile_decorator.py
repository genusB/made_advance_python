import cProfile
from functools import wraps


def profile_deco(func):
    def print_stat():
        print('Hello')

    func.print_stat = print_stat
    pr = cProfile.Profile()
    pr.enable()

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@profile_deco
def add(a, b):
    return a + b


if __name__ == '__main__':
    print(add(1, 2))
    print(add(1, 2))
    print(add(1, 2))
    print(add(1, 2))
    add.print_stat()


