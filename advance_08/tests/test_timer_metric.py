import pytest
import math
from advance_08.stats import BaseMetric, MetricTimer, Number
from sleep_func import sleep_func, sleep_func_with_error


@pytest.mark.parametrize("values, expected_value_result", [([1.0], 1.0),
                                                           ([1.0, 2.0, 3.0], 6.0),
                                                           ([0.1, 0.2, 0.3], 0.6)])
def test_add_valid_time(values, expected_value_result):
    metric: MetricTimer = MetricTimer('test')

    for value in values:
        metric.add(value)

    assert math.isclose(metric.get_value(), expected_value_result)


@pytest.mark.parametrize("value", [-1.0, 0.0, -0.01])
def test_add_invalid_timer(value):
    metric: MetricTimer = MetricTimer('test')

    with pytest.raises(ValueError) as exc_info:
        metric.add(value)

    assert str(exc_info.value) == 'Time must be greater than 0'


@pytest.mark.parametrize("sec", [1.0, 0.1])
def test_using_context_manager(sec):
    metric: MetricTimer = MetricTimer('test')

    with metric:
        res = sleep_func(sec)

    assert math.isclose(res, sec)
    assert metric.get_value() > sec


@pytest.mark.parametrize("sec", [1.0, 0.1])
def test_using_context_manager_with_error(sec):
    metric: MetricTimer = MetricTimer('test')

    with pytest.raises(ValueError):
        with metric:
            sleep_func_with_error(sec)

    assert metric.get_value() > sec


def test_clear():
    metric: MetricTimer = MetricTimer('test')

    value: Number = 0.1
    metric.add(value)

    assert math.isclose(metric.get_value(), value)

    metric.clear()

    assert not metric.get_value()


@pytest.mark.parametrize("name", ['test', 'timer'])
def test_get_name(name):
    metric: MetricTimer = MetricTimer(name)

    assert metric.get_name() == f'{name}.timer'
