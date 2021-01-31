from functools import reduce


def aflatten(lst):
    return [x for i in lst for x in i]


def bflatten(lst):
    if lst == []:
        return []
    return lst[0]+bflatten(lst[1:])


def cflatten(lst):
    return reduce(lambda a, b: a+b, lst, [])


print(aflatten([[1, 2, 3], ['a', 'b', 'c'], [1.1, 1.2, 2.3]]))
print(bflatten([[1, 2, 3], ['a', 'b', 'c'], [1.1, 1.2, 2.3]]))
print(cflatten([[1, 2, 3], ['a', 'b', 'c'], [1.1, 1.2, 2.3]]))
