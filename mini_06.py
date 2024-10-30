def flat_one_lvl(data:list):
    result = []
    for l in data:
        if isinstance(l, list):
            for j in l:
                result.append(j)
        else:
            result.append(l)
    return result;

def flatten(data:list):
    if all([(isinstance(l, list) == 0) for l in data]):
        return data;
    result = flat_one_lvl(data)
    return flatten(result)

def flatten_depth(data:list, depth:int):
    """
    >>> flatten_depth([1, 2, [4, 5], [6, [7]], 8], depth=2)
    [1, 2, 4, 5, 6, 7, 8]
    >>> flatten_depth([1, 2, [4, 5], [6, [7]], 8], depth=1)
    [1, 2, 4, 5, 6, [7], 8]
    >>> flatten_depth([1, 2, [4, 5], [6, [7]], 8], depth=1488)
    [1, 2, 4, 5, 6, 7, 8]
    """
    
    if depth == 0 or all([(isinstance(l, list) == 0) for l in data]):
        return data;
    result = flat_one_lvl(data)
    return flatten_depth(result, depth - 1)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
