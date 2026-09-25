"""
Custom LRU (Least Recently Used) Cache Implementation
Senior SDET Context: Caches expensive API query results or authentication tokens with fixed capacity using OrderedDict.
"""

from collections import OrderedDict
from typing import Any

class LRUCache:
    def __init__(self, capacity: int = 3):
        self.capacity = capacity
        self.cache: OrderedDict[str, Any] = OrderedDict()

    def get(self, key: str) -> Any:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: str, value: Any) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

if __name__ == "__main__":
    cache = LRUCache(capacity=2)
    cache.put("token_qa", "Bearer token_123")
    cache.put("token_prod", "Bearer token_456")
    print("Get token_qa:", cache.get("token_qa"))
    cache.put("token_staging", "Bearer token_789")
    print("Get token_prod (evicted):", cache.get("token_prod"))
    print("Get token_staging:", cache.get("token_staging"))
