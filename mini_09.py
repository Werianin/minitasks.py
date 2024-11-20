class LRUCache:
    def __init__(self, capacity=16):
        self.cache = {}
        self.popularity = {}
        self.cap = capacity
        self.len = 0

    def put(self, key, value):
        if self.len == self.cap:
            val = max(self.cache.values())
            k = self.popularity.values().index(val)
            self.cache.pop(k)
            self.popularity.pop(k)
            self.len -= 1
        self.cache[key] = value
        self.popularity[key] = 0
        self.len += 1

    def get(self, key):
        if key in self.cache.keys():
            self.popularity[key] = 0
            for k in self.cache.keys():
                if k != key:
                    self.popularity[k] += 1
            return self.cache[key]
        return None


def memoize(f):
    c = LRUCache(capacity=2)

    def inner(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))

        if not c.get(key):
            c.put(c, key, f(*args, **kwargs))

        return c.get(key)

    inner.__name__ = f.__name__
    inner.__doc__ = f.__doc__
    inner.__module__ = f.__module__

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
