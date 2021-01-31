def compose(*args):
    def inside(n):
        string = ''
        for i in range(len(args)):
            string += str(args[i].__name__)+'('
        string += str(n)+')'*len(args)
        return eval(string)
    return inside


def square(n):
    return n**2


def takefunc(func):
    return func(2)


def inscrease(n):
    return n+1


f = compose(inscrease, square)
print(f(3))
print(eval('inscrease(square(3))'))
