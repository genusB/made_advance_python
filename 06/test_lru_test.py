import unittest
import lru_cache


class TestLRUCache(unittest.TestCase):
    def test_set_get_values(self):
        cache = lru_cache.LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

    def test_update_queue(self):
        cache = lru_cache.LRUCache(3)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")

        cache.get("k2")

        self.assertListEqual(cache.queue, ["k1", "k3", "k2"])

        cache.get("k1")

        self.assertListEqual(cache.queue, ["k3", "k2", "k1"])

    def test_capacity_zero(self):
        with self.assertRaises(ValueError):
            lru_cache.LRUCache(0)

    def test_capacity_one(self):
        cache = lru_cache.LRUCache(1)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), None)

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

        cache.set("k4", "val4")

        self.assertIs(cache.get("k3"), None)
        self.assertEqual(cache.get("k4"), "val4")
        self.assertEqual(cache.get("k1"), "val1")

    def test_full_replacement(self):
        cache = lru_cache.LRUCache(3)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")

        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")
        self.assertListEqual(cache.queue, ["k3", "k2", "k1"])

        cache.set("k4", "val4")
        cache.set("k5", "val5")
        cache.set("k6", "val6")

        self.assertEqual(cache.get("k4"), "val4")
        self.assertEqual(cache.get("k5"), "val5")
        self.assertEqual(cache.get("k6"), "val6")
        self.assertListEqual(cache.queue, ["k4", "k5", "k6"])

    def test_change_existing_key(self):
        cache = lru_cache.LRUCache(3)

        cache.set("k1", "val1.1")
        cache.set("k2", "val2.1")
        cache.set("k3", "val3.1")

        self.assertEqual(cache.get("k1"), "val1.1")
        self.assertEqual(cache.get("k2"), "val2.1")
        self.assertEqual(cache.get("k3"), "val3.1")
        self.assertListEqual(cache.queue, ["k1", "k2", "k3"])

        cache.set("k1", "val1.2")

        self.assertEqual(cache.get("k1"), "val1.2")
        self.assertListEqual(cache.queue, ["k2", "k3", "k1"])


if __name__ == "__main__":
    unittest.main()