from functools import reduce


def flatten(lst):
    '''2. a'''
    return [item for sub_lst in lst for item in sub_lst]


def flatten(lst):
    '''2. b'''
    if not lst:
        return []
    return lst[0] + flatten(lst[1:])


def flatten(lst):
    '''2. c'''
    return list(reduce(lambda x, y: x + y, lst, []))
