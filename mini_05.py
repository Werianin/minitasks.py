def specialize(foo, *args, **kwargs):
    """
    >>> def s(x, y): return x + y
    >>> specialize(s, y=1)(10)
    11
    >>> specialize(s, 1, 1)()
    2
    >>> specialize(s, 'sys')('pro')
    'syspro'
    >>> def m(x, y): return x % y
    >>> specialize(m, y=2)(5)
    1
    >>> specialize(m, 42)(17)
    8
    """

    def result(*args_new, **kwargs_new):
        return foo(*args, *args_new,
                   **kwargs, **kwargs_new)
    return result



if __name__ == "__main__":
    import doctest

    doctest.testmod()
