def lessThan(n, lst):
    '''3. a'''
    return [i for i in lst if i < n]


def lessThan(n, lst):
    '''3. b'''
    if not lst:
        return []
    return [lst[0]] + lessThan(n, lst[1:]) if lst[0] < n else lessThan(n, lst[1:])


def lessThan(n, lst):
    '''3. c'''
    return list(filter(lambda x: x < n, lst))
