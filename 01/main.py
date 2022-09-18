from math import sqrt


def solve_equation(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2*a)
    else:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2*a)
        return x1, x2


def split_numbers(arr):
    odd = []
    even = []
    for i in arr:
        odd.append(i) if i % 2 == 0 else even.append(i)

    return odd, even


def solve_equation_test():
    assert solve_equation(1, 2, -3) == (1, -3)
    assert solve_equation(1, -10, 21) == (7, 3)
    assert solve_equation(3, -14, -5) == (5, -0.3333333333333333)
    assert solve_equation(3, -18, 27) == 3
    assert solve_equation(2, -20, 100) is None


def split_numbers_test():
    assert split_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])
    assert split_numbers([]) == ([], [])
    assert split_numbers([1, 3, 5]) == ([], [1, 3, 5])


solve_equation_test()
split_numbers_test()




