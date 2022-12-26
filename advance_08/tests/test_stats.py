import pytest
from advance_08.stats import Stats, MetricCount, MetricTimer, MetricAvg, Number


def test_empty_collect():
    assert Stats.collect() == {}
    assert type(Stats.collect()) is dict


def test_collect_with_metrics():
    Stats.count("http_get_data").add()
    Stats.avg("http_get_data").add(0.7)

    metrics = Stats.collect()

    assert metrics == {
        "http_get_data.count": 1,
        "http_get_data.avg": 0.7,
    }

    assert Stats.collect() == {}


def test_no_used_collect():
    Stats.count("no_used")
    Stats.avg("no_used")

    assert Stats.collect() == {}


@pytest.mark.parametrize("name", ['test', 'timer'])
def test_timer(name):
    metric = Stats.timer(name)

    assert type(metric) is MetricTimer

    Stats.timer(name).add(0.1)

    assert Stats.timer(name) is metric


@pytest.mark.parametrize("name", ['test', 'avg'])
def test_avg(name):
    metric = Stats.avg(name)

    assert type(metric) is MetricAvg

    Stats.avg(name).add(0.1)

    assert Stats.avg(name) is metric


@pytest.mark.parametrize("name", ['test', 'count'])
def test_timer(name):
    metric = Stats.count(name)

    assert type(metric) is MetricCount

    Stats.count(name).add()

    assert Stats.count(name) is metric

