def take(iter, n):
    res = []
    for i in range(n):
        res.append(next(iter))
    return res


# 11.1
def cycle(iterable):
    """
    >>> take(cycle([1, 2, 3]), 10)
    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
    """
    items = list(iterable)
    while True:
        yield from items


# 11.2
def chain(*iterables):
    """
    >>> list(chain([1, 2, 3], ['a', 'b']))
    [1, 2, 3, 'a', 'b']
    >>> take(cycle(chain([1, 2, 3], ["A", "c"], ("Z", "f"))), 10)
    [1, 2, 3, 'A', 'c', 'Z', 'f', 1, 2, 3]
    """
    for iterable in iterables:
        yield from iterable


if __name__ == "__main__":
    import doctest

    doctest.testmod()
