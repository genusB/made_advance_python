import pytest
from advance_08.stats import BaseMetric, MetricCount, Number


@pytest.mark.parametrize("times_to_add", [1, 2, 3])
def test_add_count(times_to_add):
    metric: MetricCount = MetricCount('test')

    for _ in range(times_to_add):
        metric.add()

    assert metric.get_value() == times_to_add


@pytest.mark.parametrize("times_to_add", [-2, 3, 0])
def test_add_count_with_param(times_to_add):
    metric: MetricCount = MetricCount('test')

    with pytest.raises(ValueError) as exc_info:
        metric.add(times_to_add)

    assert str(exc_info.value) == 'Increment is automatically set to 1'


def test_clear():
    metric: MetricCount = MetricCount('test')
    metric.add()

    assert metric.get_value() == 1

    metric.clear()

    assert not metric.get_value()


@pytest.mark.parametrize("name", ['test', 'count'])
def test_get_name(name):
    metric: MetricCount = MetricCount(name)

    assert metric.get_name() == f'{name}.count'


