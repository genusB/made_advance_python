import cProfile
import io
import pstats
import time
from functools import wraps


def profile_deco(func):
    def print_stat():
        print(*profile_stats)

    func.print_stat = print_stat
    profile_stats = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        prof = cProfile.Profile()
        prof.enable()
        res = func(*args, **kwargs)

        s = io.StringIO()
        sortby = "cumulative"
        stats = pstats.Stats(prof, stream=s).sort_stats(sortby)
        stats.print_stats()
        profile_stats.append(s.getvalue())

        return res

    return wrapper


@profile_deco
def add(a, b, sleep):
    time.sleep(sleep)
    return a + b


if __name__ == '__main__':
    print(add(1, 2, 0.5))
    print(add(1, 2, 0.1))
    print(add(1, 2, 0.3))
    print(add(1, 2, 0.2))
    add.print_stat()


