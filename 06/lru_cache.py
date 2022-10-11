import queue


class LRUCache:

    def __init__(self, capacity=42):
        if capacity == 0:
            raise ValueError("Capacity must be greater than zero")
        self.capacity = capacity
        self.cache = {}
        self.queue = []

    def get(self, key):
        if key not in self.cache:
            return None

        index_to_remove = self.queue.index(key)
        self.queue.append(self.queue.pop(index_to_remove))
        return self.cache[key]

    def set(self, key, value):
        if len(self.queue) == self.capacity:
            key_to_remove = self.queue.pop(0)
            self.cache.pop(key_to_remove, None)
        self.queue.append(key)
        self.cache[key] = value
