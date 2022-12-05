import cProfile
import io
import pstats
import time
import weakref
from memory_profiler import profile


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointColorClassic:
    def __init__(self, x, y, color):
        self.point = Point(x, y)
        self.color = color


class PointColorWeakref:
    def __init__(self, x, y, color):
        point = Point(x, y)
        self.point = weakref.ref(point)()
        self.color = color


class PointColorSlots:
    __slots__ = ('point', 'color',)

    def __init__(self, x, y, color):
        self.point = Point(x, y)
        self.color = color


@profile
def create_objects(cls, N):
    start = time.process_time()
    points = [cls(i, i, 'red') for i in range(N)]
    print(time.process_time() - start)
    return points


@profile
def time_change_points(points):
    start = time.process_time()
    for point in points:
        point.point.x += 1
        point.point.y += 1
    print(time.process_time() - start)


@profile
def time_change_color(points):
    start = time.process_time()
    for point in points:
        point.color = 'some'
    print(time.process_time() - start)


@profile
def time_delete_color(points):
    start = time.process_time()
    for point in points:
        del point.color
    print(time.process_time() - start)


def main():
    N = 1_000_000

    print('Order of the classes: PointColorClassic, PointColorWeakref, PointColorSlots')
    print('=============================================')

    print(f'Creating {N} objects')

    pr = cProfile.Profile()
    pr.enable()

    color_points_classic = create_objects(PointColorClassic, N)
    color_points_weakref = create_objects(PointColorWeakref, N)
    color_points_slots = create_objects(PointColorSlots, N)

    print(f"Changing property of {N} object's properties")

    time_change_points(color_points_classic)
    time_change_points(color_points_weakref)
    time_change_points(color_points_slots)

    print(f'Changing property of {N} objects')

    time_change_color(color_points_classic)
    time_change_color(color_points_weakref)
    time_change_color(color_points_slots)

    print(f'Deleting property of {N} objects')

    time_delete_color(color_points_classic)
    time_delete_color(color_points_weakref)
    time_delete_color(color_points_slots)

    pr.disable()

    s = io.StringIO()
    sortby = "cumulative"
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()

    print(s.getvalue())


if __name__ == '__main__':
    main()




