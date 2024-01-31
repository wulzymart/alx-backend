#!/usr/bin/python3
"""Create a class LIFOCache that inherits from BaseCaching
and is a caching system:"""


BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """FIFO caching system"""

    def __init__(self):
        """initialize instance"""
        super().__init__()

    def put(self, key, item):
        """puts an item in cache"""
        if not key or not item:
            return
        keys = list(self.cache_data.keys())
        if len(keys) >= BaseCaching.MAX_ITEMS and\
                key not in keys:
            last = keys[-1]
            del self.cache_data[last]
            print(f"DISCARD: {last}")
        self.cache_data[key] = item

    def get(self, key):
        """gets a key from the cache"""
        if not key:
            return
        return self.cache_data.get(key)
