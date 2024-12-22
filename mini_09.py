from collections import OrderedDict
from functools import wraps


class LRUCache:
    def __init__(self, capacity=16):
        self.cache = OrderedDict()
        self.cap = capacity

    def put(self, key, value):
        if len(self.cache) == self.cap:
            self.cache.popitem()
        self.cache[key] = value

    def get(self, key):
        if key in self.cache.keys():
            self.cache.move_to_end(key, last=False)
            return self.cache[key]
        return None


def memoize(f):
    c = LRUCache(capacity=2)

    @wraps(f)
    def inner(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))

        if not c.get(key):
            c.put(c, key, f(*args, **kwargs))

        return c.get(key)

    return inner


@memoize
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


"""
>>> fib(250)
7896325826131730509282738943634332893686268675876375
"""
if __name__ == "__main__":
    import doctest

    doctest.testmod()
