# https://leetcode.com/problems/lru-cache
import collections

class LRUCache:

    def __init__(self, capacity: int):
        self._dict = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self._dict:
            return -1
        value = self._dict.pop(key)
        self._dict[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self._dict:
            self._dict.pop(key)
        elif len(self._dict) == self.capacity:
            self._dict.popitem(last=False)
        self._dict[key] = value
