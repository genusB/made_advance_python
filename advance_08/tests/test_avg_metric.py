import pytest
import math
from advance_08.stats import MetricAvg, Number


@pytest.mark.parametrize("values, expected_value_result", [([1.0], 1.0),
                                                           ([2.0, 2.0, 2.0], 2.0),
                                                           ([1.2, 1.5, 2.7], 1.8),
                                                           ([-1.2, -1.5, 2.7], 0.0),
                                                           ([-1.2, -1.5, 3.0], 0.1)])
def test_add_avg(values, expected_value_result):
    metric: MetricAvg = MetricAvg('test')

    for value in values:
        metric.add(value)

    assert math.isclose(metric.get_value(), expected_value_result)


def test_clear():
    metric: MetricAvg = MetricAvg('test')

    value: Number = 0.1
    metric.add(value)

    assert math.isclose(metric.get_value(), value)

    metric.clear()

    assert not metric.get_value()
    assert len(metric.all_passed_vals) == 0


@pytest.mark.parametrize("name", ['test', 'avg'])
def test_get_name(name):
    metric: MetricAvg = MetricAvg(name)

    assert metric.get_name() == f'{name}.avg'

