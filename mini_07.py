import functools


def deprecated(func=None, *, since=None, will_be_removed=None):
    if func is None:
        return functools.partial(deprecated,
                                 since=since, will_be_removed=will_be_removed)
    """
        >>> def bar(): print("Hello from bar")
        >>> bar = deprecated(bar)
        >>> bar()
        Warning: function bar is deprecated. It will be removed in future versions.
        Hello from bar

        >>> def sum(x, y): print(f"{x} + {y} = {x + y}")
        >>> sum = deprecated(sum, since="4.0.2")
        >>> sum(4, 2)
        Warning: function sum is deprecated since version 4.0.2. It will be removed in future versions.
        4 + 2 = 6

        >>> def min(x, y): print(f"{x} < {y}") if x <= y else print(f"{y} < {x}")
        >>> min = deprecated(min, will_be_removed="4.2.0")
        >>> min(2, 4)
        Warning: function min is deprecated. It will be removed in version 4.2.0.
        2 < 4

        >>> def max(x, y): print(f"{x} > {y}") if x >= y else print(f"{y} > {x}")
        >>> max = deprecated(max, since="4.0.2", will_be_removed="4.2.0")
        >>> max(2, 4)
        Warning: function max is deprecated since version 4.0.2. It will be removed in version 4.2.0.
        4 > 2
    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        warning = f"Warning: function {func.__name__} is deprecated"
        if since:
            warning += f" since version {since}"
            warning += '.'
        if will_be_removed:
            warning += f" It will be removed in version {will_be_removed}."
        else:
            warning += " It will be removed in future versions."
        print(warning)
        func(*args, **kwargs)
    return inner


@deprecated
def foo():
    print("Hello from foo")

foo()

if __name__ == "__main__":
    import doctest

    doctest.testmod()
