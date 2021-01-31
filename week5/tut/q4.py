from functools import reduce


def compose(*args):
    def inside(n):
        if (len(args) == 1):
            return args[0](n)
        else:
            return args[0](compose(*args[1:])(n))
    return inside


def bcompose(*args):
    return lambda x: reduce(lambda a, b: b(a), args[::-1], x)


def inscrease(n):
    return n+1


def double(n):
    return n*2


def square(n):
    return n*n


funcList = (inscrease, double, square)
f = compose(*funcList)
bf = bcompose(*funcList)
print(f(3))
print(bf(3))
