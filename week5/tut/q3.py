def alessThan(n, lst):
    return [i for i in lst if i < n]


def blessThan(n, lst):
    return [] if lst == [] else (blessThan(n, lst[1:]) if lst[0] > n else [lst[0]] + blessThan(n, lst[1:]))


def clessThan(n, lst):
    return list(filter(lambda x: x < n, lst))


print(alessThan(50, [1, 55, 6, 2]))
print(blessThan(50, [1, 55, 6, 2]))
print(clessThan(50, [1, 55, 6, 2]))
