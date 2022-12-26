import time


def sleep_func(sec: float) -> float:
    time.sleep(sec)
    return sec


def sleep_func_with_error(sec: float):
    time.sleep(sec)
    raise ValueError('wrong')