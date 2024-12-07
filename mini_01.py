def fun(n):
    count = 0
    value = 1
    if (n < 0):
        count += 1
        n = -n - 1
        value = 0
    while (n != 0):
        if (n % 2 == value):
            count += 1
        n //= 2
    return count


def tests():
    assert fun(10) == 2
    assert fun(-123) == 3
    assert fun(0) == 0

    print('All tests passed')


tests()
