import sys

from logging_config import create_root_loger
from logging_config import create_total_loger


class LRUCache:
    def __init__(self, capacity=42):
        if "-s" in sys.argv:
            self.logger = create_total_loger()
        else:
            self.logger = create_root_loger()

        if capacity == 0:
            message = "Capacity must be greater than zero"
            self.logger.critical(message)
            raise ValueError(message)

        self.capacity = capacity
        self.cache = {}
        self.queue = []

        self.logger.debug("Init was finished successfully")

    def get(self, key):
        if key not in self.cache:
            self.logger.warning("Key is not in cache")
            return None

        index_to_remove = self.queue.index(key)
        self.queue.append(self.queue.pop(index_to_remove))
        return self.cache[key]

    def set(self, key, value):
        if len(self.queue) == self.capacity:
            key_to_remove = self.queue.pop(0)
            self.cache.pop(key_to_remove, None)
            self.logger.info(f"{key_to_remove} was removed from cache")
        self.queue.append(key)
        self.cache[key] = value
        self.logger.info(f"Value by key '{key}' was added to cache")
