import json
import time
from functools import wraps


def parse_json(json_str: str, required_fields=None, keywords=None, keyword_callback=None):
    json_doc = json.loads(json_str)
    for key in json_doc:
        if required_fields and keywords and key in required_fields:
            for keyword in keywords:
                if keyword in json_doc[key].split():
                    keyword_callback(keyword)


def mean(k=1):
    time_of_last_calls = []

    def _mean(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.process_time()
            res = func(*args, **kwargs)
            delta = time.process_time() - start
            time_of_last_calls.append(delta)

            if len(time_of_last_calls) >= k:
                print(sum(time_of_last_calls[-k:]) / k)
            return res

        return wrapper

    return _mean


def parse_json_test():
    stat = {}

    def statistic_callback(keyword):
        counter = stat.get(keyword, 0)
        stat[keyword] = counter + 1

    json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
    parse_json(json_str, ["key1", "key2"], ["word2", "word3"], statistic_callback)

    assert stat == {'word2': 2, 'word3': 1}

    stat = {}
    json_str = '{"key1": "Word1 word2less", "key2": "word2 word3"}'
    parse_json(json_str, ["key1", "key2"], ["word1", "word2"], statistic_callback)

    assert stat == {'word2': 1}

    stat = {}
    json_str = '{"key1": "Word1 word2less", "key2": "word2 word3"}'
    parse_json(json_str, ["key1", "key2"], ["word1", "word22"], statistic_callback)

    assert not stat


parse_json_test()


@mean(2)
def test_func_pass():
    pass


@mean(10)
def test_func_without_args():
    return 1


@mean(10)
def test_func_with_args(arr):
    return sum(arr)


for i in range(15):
    test_func_pass()

for i in range(15):
    print(test_func_without_args())

for i in range(15):
    print(test_func_with_args([i for i in range(100)]))


