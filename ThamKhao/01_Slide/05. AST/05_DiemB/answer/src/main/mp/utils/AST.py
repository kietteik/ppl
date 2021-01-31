from abc import ABC, abstractmethod, ABCMeta
from Visitor import Visitor


class AST(ABC):
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        return v.visit(self, param)

class Expr(AST):
    __metaclass__ = ABCMeta
    pass



class Add(Expr):
    #left:Expr
    #right:Expr
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "Add(" + str(self.left) + "," + str(self.right) + ")"

    def accept(self, v, param):
        return v.visitAddOp(self, param)

class Minus(Expr):
    #left:Expr
    #right:Expr
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "Minus(" + str(self.left) + "," + str(self.right) + ")"

    def accept(self, v, param):
        return v.visitMinusOp(self, param)

class Mul(Expr):
    #left:Expr
    #right:Expr
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "Mul(" + str(self.left) + "," + str(self.right) + ")"

    def accept(self, v, param):
        return v.visitMulOp(self, param)

class Div(Expr):
    #left:Expr
    #right:Expr
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "Div(" + str(self.left) + "," + str(self.right) + ")"

    def accept(self, v, param):
        return v.visitDivOp(self, param)




class Id(Expr):
    #value:string
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Id(" + self.value + ")"

    def accept(self, v, param):
        return v.visitId(self, param)

class IntLiteral(Expr):
    #value:int
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "IntLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitIntLiteral(self, param)

class BooleanLiteral(Expr):
    #value:boolean
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "BooleanLiteral(" + str(self.value) + ")"

    def accept(self, v, param):
        return v.visitBooleanLiteral(self, param)
