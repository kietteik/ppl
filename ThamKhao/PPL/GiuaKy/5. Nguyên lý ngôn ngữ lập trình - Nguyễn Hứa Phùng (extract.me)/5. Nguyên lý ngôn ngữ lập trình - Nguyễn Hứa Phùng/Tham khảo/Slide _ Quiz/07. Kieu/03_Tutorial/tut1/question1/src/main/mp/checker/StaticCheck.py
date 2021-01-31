
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
import collections


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return 'MType(['+','.join(str(i) for i in self.partype)+']'+','+str(self.rettype)+')'


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return 'Symbol('+self.name+','+str(self.mtype)+')'


class StaticChecker(BaseVisitor, Utils):


    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, [])

    def visitProgram(self, ast, c):
        return [self.visit(x, c) for x in ast.decl[::-1] ]


    def visitVarDecl(self, ast, c):
        return Symbol(ast.variable.name, ast.varType)


    def visitFuncDecl(self,ast, c): 
        return Symbol(ast.name.name, MType([i.varType for i in ast.param], ast.returnType))

