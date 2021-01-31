def double(lst):
    '''1. a'''
    return [i * 2 for i in lst]
def double(lst):
    '''1. b'''
    if not lst: return []
    return [lst[0] * 2] + double(lst[1:])
def double(lst):
    '''1. c'''
    return list(map(lambda x: x * 2, lst))

def flatten(lst):
    '''2. a'''
    return [item for sub_lst in lst for item in sub_lst]
def flatten(lst):
    '''2. b'''
    if not lst: return []
    return lst[0] + flatten(lst[1:])
from functools import reduce
def flatten(lst):
    '''2. c'''
    return list(reduce(lambda x, y: x + y, lst, []))

def lessThan(n, lst):
    '''3. a'''
    return [i for i in lst if i < n]
def lessThan(n, lst):
    '''3. b'''
    if not lst: return []
    return [lst[0]] + lessThan(n, lst[1:]) if lst[0] < n else lessThan(n, lst[1:])
def lessThan(n, lst):
    '''3. c'''
    return list(filter(lambda x: x < n, lst))

def compose(*args):
    '''4. a'''
  return lambda x: x if not args else args[0](compose(*args[1:])(x))

from functools import reduce
def compose(*args):
    '''4. b'''
    return lambda x: reduce(lambda x, y: y(x), args[::-1], x)
