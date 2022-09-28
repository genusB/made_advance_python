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
    def _mean(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.process_time()
            for i in range(k):
                func(*args, **kwargs)
            return time.process_time() - start
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

@mean(10000)
def test_func_without_args():
    pass


@mean(10000)
def test_func_with_args(arr):
    for i in arr:
        pass


print(test_func_without_args())
print(test_func_with_args([i for i in range(100)]))








