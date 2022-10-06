import unittest
import lru_cache


class TestLRUCache(unittest.TestCase):
    def test_set_get_values(self):
        cache = lru_cache.LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

    def test_get_not_existing_values(self):
        cache = lru_cache.LRUCache(3)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertIs(cache.get("k3"), None)
        self.assertIs(cache.get(4), None)

    def test_cache_overflow(self):
        cache = lru_cache.LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k3", "val3")

        self.assertEqual(cache.get("k3"), "val3")
        self.assertIs(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val1")


if __name__ == "__main__":
    unittest.main()