def invert(data: dict):
    """
    >>> invert({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832})
    {97832: ('Ivanov', 'Kuznecov'), 55521: 'Petrov'}
    >>> invert({"Ivanov": 97832, "Petrov": 97832, "Kuznecov": 97832})
    {97832: ('Ivanov', 'Petrov', 'Kuznecov')}
    >>> invert({("Ivanov",): 97832, "Petrov": 55521, "Kuznecov": 97832})
    {97832: (('Ivanov',), 'Kuznecov'), 55521: 'Petrov'}
    >>> invert({})
    {}
    """
    res = {}
    for key, val in data.items():
        if val not in res.keys():
            res[val] = key
        elif res.get(val) in data.keys():
            res[val] = (res.get(val),) + (key,)
        else:
            res[val] = res.get(val) + (key,)
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
