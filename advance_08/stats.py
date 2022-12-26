import time
from types import TracebackType
from typing import Optional, Type

Number = int | float


class BaseMetric:
    def __init__(self, name: str):
        self.name: str = name
        self.value: Number | None = None
        self.class_name: str = 'basic'

    def get_name(self) -> str:
        return f'{self.name}.{self.class_name}'

    def get_value(self) -> None | Number:
        return self.value

    def add(self, value: Number) -> None:
        pass

    def clear(self) -> None:
        self.value = None


class MetricTimer(BaseMetric):
    def __init__(self, name: str):
        super().__init__(name)
        self.class_name: str = 'timer'

    def add(self, value: Number) -> None:
        if value <= 0:
            raise ValueError('Time must be greater than 0')

        if not self.value:
            self.value = 0

        self.value += value
        super().add(value)

    def __enter__(self):
        self.time_start = time.time()
        return self

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> Optional[bool]:
        self.add(time.time() - self.time_start)
        if not exc:
            return True
        else:
            return False


class MetricAvg(BaseMetric):
    def __init__(self, name: str):
        super().__init__(name)
        self.class_name: str = 'avg'
        self.all_passed_vals: list = []

    def add(self, value: Number) -> None:
        self.all_passed_vals.append(value)
        self.value = sum(self.all_passed_vals) / len(self.all_passed_vals)

    def clear(self) -> None:
        super().clear()
        self.all_passed_vals = []


class MetricCount(BaseMetric):
    def __init__(self, name: str):
        super().__init__(name)
        self.class_name: str = 'count'

    def add(self, value: Number = 1) -> None:
        if value != 1:
            raise ValueError('Increment is automatically set to 1')

        if not self.value:
            self.value = 0

        self.value += value


class Stats:
    metrics: list[BaseMetric] = []

    @classmethod
    def get_or_create_metric(cls, name, postfix_name, metric_cls) -> BaseMetric:
        metric: BaseMetric = next(filter(lambda m: m.get_name() == f'{name}.{postfix_name}', cls.metrics),
                                  metric_cls(name))

        if metric not in cls.metrics:
            cls.metrics.append(metric)

        return metric

    @classmethod
    def timer(cls, name: str) -> BaseMetric:
        return cls.get_or_create_metric(name, 'timer', MetricTimer)

    @classmethod
    def avg(cls, name: str) -> BaseMetric:
        return cls.get_or_create_metric(name, 'avg', MetricAvg)

    @classmethod
    def count(cls, name: str) -> BaseMetric:
        return cls.get_or_create_metric(name, 'count', MetricCount)

    @classmethod
    def collect(cls) -> dict:
        metrics: dict = {metric.get_name(): metric.get_value() for metric in cls.metrics if metric.get_value()}

        for metric in cls.metrics:
            metric.clear()

        return metrics
