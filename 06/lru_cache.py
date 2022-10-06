import queue


class LRUCache:

    def __init__(self, capacity=42):
        self.capacity = capacity
        self.cache = {}
        self.queue = queue.LifoQueue(maxsize=capacity)

    def get(self, key):
        if key not in self.cache:
            return None
        self.queue.put(self.queue.get())
        return self.cache[key]

    def set(self, key, value):
        if self.queue.qsize() == self.capacity:
            key_to_remove = self.queue.get()
            self.cache[key_to_remove] = None
        self.queue.put(key)
        self.cache[key] = value


