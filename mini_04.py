def fun(data:dict):
    res = {}
    for key in data.keys():
        if data[key] not in res.keys():
            res[data[key]] = key 
        else:
            if type(res[data[key]]) is tuple:
                res[data[key]] = res[data[key]] + (key,)
            else:
                res[data[key]] = (res[data[key]],) + (key,)
    return res


def tests():
    assert fun({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832}) == {97832: ('Ivanov', 'Kuznecov'), 55521: 'Petrov'}
    assert fun({"Ivanov": 97832, "Petrov": 97832, "Kuznecov": 97832}) == {97832: ('Ivanov', 'Petrov', 'Kuznecov')}
    assert fun({}) == {}

    print('All tests passed')


tests()
