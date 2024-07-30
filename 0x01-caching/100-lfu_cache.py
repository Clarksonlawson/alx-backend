#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import defaultdict

class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching and implements LFU caching algorithm
    """
    
    def __init__(self):
        """ Initialize LFUCache
        """
        super().__init__()
        self.frequency = defaultdict(int)  # Frequency counter for keys
        self.recent_keys = []  # To track the order of accesses

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                lfu_keys = [k for k, v in self.frequency.items() if v == min(self.frequency.values())]
                if len(lfu_keys) > 1:
                    for k in self.recent_keys:
                        if k in lfu_keys:
                            discard_key = k
                            break
                else:
                    discard_key = lfu_keys[0]
                
                print("DISCARD: {}".format(discard_key))
                del self.cache_data[discard_key]
                del self.frequency[discard_key]
                self.recent_keys.remove(discard_key)
            
            self.cache_data[key] = item
            self.frequency[key] = 1
        
        if key in self.recent_keys:
            self.recent_keys.remove(key)
        self.recent_keys.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        
        self.frequency[key] += 1
        if key in self.recent_keys:
            self.recent_keys.remove(key)
        self.recent_keys.append(key)
        
        return self.cache_data[key]

