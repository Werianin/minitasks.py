def flat_one_lvl(data: list):
    result = []
    for l in data:
        if isinstance(l, list):
            result.extend(l)
        else:
            result.append(l)
    return result


def flatten(data: list, depth=-1):
    """
    >>> flatten([1, 2, [4, 5], [6, [7]], 8])
    [1, 2, 4, 5, 6, 7, 8]
    >>> flatten([1, 2, [4, 5], [6, [7]], 8], depth=2)
    [1, 2, 4, 5, 6, 7, 8]
    >>> flatten([1, 2, [4, 5], [6, [7]], 8], depth=1)
    [1, 2, 4, 5, 6, [7], 8]
    >>> flatten([1, 2, [4, 5], [6, [7]], 8], depth=10000)
    [1, 2, 4, 5, 6, 7, 8]
    """

    if depth == 0:
        return data
    result = flat_one_lvl(data)
    if result == data:
        return data
    return flatten(result, depth - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
