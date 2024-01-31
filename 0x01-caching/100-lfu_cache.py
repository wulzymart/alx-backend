#!/usr/bin/python3
"""Create a class LFUCache that inherits from BaseCaching
and is a caching system:"""


BaseCaching = __import__("base_caching").BaseCaching


def find(obj, item):
    """find the first key with item"""
    for key, value in obj.items():
        if item == value:
            return key


class LFUCache(BaseCaching):
    """implement LRU cache system"""

    def __init__(self):
        """initialize"""
        super().__init__()
        self.recently_used = {}

    def put(self, key, item):
        """Save an item in cache"""
        if not key or not item:
            return
        if key in self.recently_used:
            current_count = self.recently_used[key]
            del self.recently_used[key]
            self.recently_used[key] = current_count + 1
            self.cache_data[key] = item
        else:
            if len(self.recently_used) >= BaseCaching.MAX_ITEMS:
                for_remove = find(
                    self.recently_used, min(self.recently_used.values()))
                del self.recently_used[for_remove]
                print(f"DISCARD: {for_remove}")
                del self.cache_data[for_remove]
                self.cache_data[key] = item
                self.recently_used[key] = 1
            else:
                self.cache_data[key] = item
                self.recently_used[key] = 1

    def get(self, key):
        """gets a key from the cache"""
        if not key or key not in self.recently_used:
            return
        current_count = self.recently_used[key]
        del self.recently_used[key]
        self.recently_used[key] = current_count + 1
        return self.cache_data.get(key)
