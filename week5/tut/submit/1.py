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