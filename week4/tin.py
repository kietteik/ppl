class Exp:
    def eval(self):
        return eval(str(self))

    # def printPrefix(self):
    #     print(self.printPrefix())


class IntLit(Exp):
    def __init__(self, num):
        self.num = num

    # @override
    def __str__(self):
        return str(self.num)

class FloatLit(Exp):
    def __init__(self, num):
        self.num = num

    # @override
    def __str__(self):
        return str(self.num)

class UnExp(Exp):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand
    
    def __str__(self):
        return self.operator + str(self.operand)

class BinExp(Exp):
    def __init__(self, left,operator, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + " " + self.operator + " " + str(self.right)


if __name__ == '__main__':
    # t = BinExp(IntLit(3),'*', BinExp(2,'+', FloatLit(0.2)))
    # print(t)
    # t.eval()

    x = BinExp(IntLit(3), '+', BinExp(IntLit(4), '*', FloatLit(2.0)))
    print(x)
    print(x.eval())