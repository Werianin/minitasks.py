def take(seq, n):
    res = []
    for i in range(n):
        res.append(next(seq))
    return res


# 11.1
def cycle(iterable):
    """
    >>> take(cycle([1, 2, 3]), 10)
    [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
    """
    while True:
        for item in iterable:
            yield item


# 11.2
def chain(*iterables):
    """
    >>> list(chain([1, 2, 3], ['a', 'b']))
    [1, 2, 3, 'a', 'b']
    """
    for iterable in iterables:
        for item in iterable:
            yield item


if __name__ == "__main__":
    import doctest

    doctest.testmod()
