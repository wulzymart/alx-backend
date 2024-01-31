#!/usr/bin/python3
"""Create a class BasicCache that inherits from BaseCaching
and is a caching system:"""


BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """caching system with get and put"""

    def put(self, key, item):
        """Assigns an object to the cache"""
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """gets a key from the cache"""
        if not key:
            return
        return self.cache_data.get(key)
