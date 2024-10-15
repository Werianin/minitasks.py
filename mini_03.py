def fun(data):
    temp = data.split('|')
    for i in range(len(temp)):
        temp[i] = temp[i].split()
        for j in range(len(temp[i])):
            temp[i][j] = float(temp[i][j])
    return temp


def tests():
    assert fun("1 2 | 3 4") == [[1.0, 2.0], [3.0, 4.0]]
    assert fun("") == [[]]

    print("All tests passed")


tests()
