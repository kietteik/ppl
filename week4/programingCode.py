class Exp:
    # def __init__(self, string):
    #     self.exp = string
    def accept(self, visit):
        return visit.visitor(self)

    def eval(self):
        return eval(str(self))

    # def printPrefix(self):
    #     print(str(self.printPrefix()))


class BinExp(Exp):
    def __init__(self, left, op, right):
        self.op = op
        self.left = left
        self.right = right

    def printPrefix(self):
        return str(self.op) + " " + self.left.printPrefix()+self.right.printPrefix()

    def printPostfix(self):
        return self.left.printPostfix() + self.right.printPostfix() + str(self.op) + " "

    def __str__(self):
        return str(self.left) + str(self.op) + str(self.right)


class UnExp(Exp):
    def __init__(self, op, right):
        self.op = op
        self.right = right

    def __str__(self):
        return str(self.op)+str(self.right)

    def printPrefix(self):
        return str(self.op)+". "+self.right.printPrefix()

    def printPostfix(self):
        return self.right.printPostfix() + str(self.op)+". "


class IntLit(Exp):
    def __init__(self, number):
        self.value = number

    def __str__(self):
        return str(self.value)+" "

    def printPrefix(self):
        return str(self.value)+" "

    def printPostfix(self):
        return str(self.value)+" "


class FloatLit(Exp):
    def __init__(self, number):
        self.value = float(number)

    def __str__(self):
        return str(self.value)

    def printPrefix(self):
        return str(self.value)+" "

    def printPostfix(self):
        return str(self.value)+" "


class Eval:
    def visitor(self, a):
        return a.eval()


class PrintPrefix:
    def visitor(self, exp):
        return exp.printPrefix()


class PrintPostfix:
    def visitor(self, exp):
        return exp.printPostfix()


y = BinExp(UnExp("-", IntLit(4)), "+", BinExp(IntLit(3), "*", FloatLit(2.0)))

print(y.accept(Eval()))
print(y.accept(PrintPrefix()))
print(y.accept(PrintPostfix()))

# print(y.printPrefix())
# print(y.eval())
