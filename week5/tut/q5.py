from functools import reduce


def func(lst):
    return reduce(lambda x, y: x+str(y), lst, '')


print(func([1, 2, 3]))
