from functools import reduce


def compose(*args):
    '''4. a'''
    return lambda x: x if not args else args[0](compose(*args[1:])(x))


def compose(*args):
    '''4. b'''
    return lambda x: reduce(lambda x, y: y(x), args[::-1], x)
