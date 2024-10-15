def fun(l1:list, l2:list):
    sus = []
    for i in range(min(len(l1), len(l2))):
        sus.append((l1[i], l2[i]))
    return sus


def tests():
    assert fun([], []) == []
    assert fun([1, 2, 3], ["a", "b"]) == [(1, "a"), (2, "b")]
    assert fun(["a", "b"], [1, 2, 3]) == [('a', 1), ('b', 2)]

    print("All tests passed")


tests()

