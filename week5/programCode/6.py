from functools import reduce


def flatten(lst):
    return reduce(lambda a, b: a+b, lst, [])


print(flatten([[1, 2], [3], [4, 5, 6, 7], [8]]))
print(flatten([[]]))
print(flatten([]))
