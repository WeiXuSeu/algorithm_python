class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        from collections import OrderedDict
        self.lru = OrderedDict()
        self.capacity = capacity
        self.remain = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.lru:
            return -1
        value = self.lru.pop(key)
        self.lru[key] = value
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.lru:
            self.lru.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 0
            else:
                self.lru.popitem(last=False)
        self.lru[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
