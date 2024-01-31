#!/usr/bin/python3
"""Create a class LRUCache that inherits from BaseCaching
and is a caching system:"""


BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """implement LRU cache system"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.recently_used = []

    def put(self, key, item):
        """Save an item in cache"""
        if not key or not item:
            return
        if key in self.recently_used:
            self.recently_used.pop(self.recently_used.index(key))
            self.recently_used.append(key)
            self.cache_data[key] = item
        else:
            self.recently_used.append(key)
            if len(self.recently_used) > BaseCaching.MAX_ITEMS:
                for_remove = self.recently_used.pop(0)
                print(f"DISCARD: {for_remove}")
                del self.cache_data[for_remove]
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """gets a key from the cache"""
        if not key or key not in self.recently_used:
            return
        self.recently_used.pop(self.recently_used.index(key))
        self.recently_used.append(key)
        return self.cache_data.get(key)
