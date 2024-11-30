def coroutine(function):
    """
    >>> st = coroutine(storage)
    >>> st.send(42)
    storage size is 1
    >>> st.send(52)
    storage size is 2
    """
    def new_func(*args, **kwargs):
        gen = function(*args, **kwargs)
        next(gen)  # 😏
        return gen
    return new_func


@coroutine
def storage():
    values = set()
    while True:
        val = yield
        values.add(val)
        print(f"storage size is {len(values)}")


st = storage()
st.send(42)  # storage size is 1
st.send(52)  # storage size is 2
