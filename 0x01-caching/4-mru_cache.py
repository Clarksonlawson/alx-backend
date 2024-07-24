#!/usr/bin/env python3
""" MRU caching module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines a MRU caching system """
    
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = self.order.pop()
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")
            self.cache_data[key] = item
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key, None)
        return None

