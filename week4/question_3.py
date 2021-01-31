class Expr:
    def eval(self):
        print(eval(str(self)))


class Number(Expr):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)


class BinOp(Expr):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + " " + self.operator + " " + str(self.right)


class UnOp(Expr):
    def 


class Parentheses(Expr):
    def __init__(self, operand):
        self.operand = operand

    def __str__(self):
        return "(" + str(self.operand) + ")"


class Var(Expr):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)


if __name__ == '__main__':
    x = Number(1)
    print(x)

    t = BinOp('*', Parentheses(BinOp('+', x, 0.2)), 3)
    print(t)

    t.eval()
