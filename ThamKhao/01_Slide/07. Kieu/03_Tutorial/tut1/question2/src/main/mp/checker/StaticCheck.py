
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

    global_envi = [Symbol("getInt",MType([],IntType())),
    			   Symbol("putIntLn",MType([IntType()],VoidType()))]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def visitProgram(self, ast, c):
        t=c.copy()
        
        return [self.visit(x, t) for x in ast.decl ]


    def visitVarDecl(self, ast, c):
      
        res = self.lookup(ast.variable.name,c,lambda x: x.name)
        if res is not None:
            raise Redeclared(Variable(),res.name)
        c.append(Symbol(ast.variable.name, ast.varType))
        return Symbol(ast.variable.name, ast.varType)


    def visitFuncDecl(self,ast, c): 
        if type(ast.returnType) is not VoidType:
            if self.lookup(ast.name.name,c,lambda x: x.name) is not None:
                raise Redeclared(Function(),ast.name.name)
        else:
            if self.lookup(ast.name.name,c,lambda x: x.name) is not None:
                raise Redeclared(Procedure(),ast.name.name)
        c.append(Symbol(ast.name.name, MType([i.varType for i in ast.param], ast.returnType)))
        return Symbol(ast.name.name, MType([i.varType for i in ast.param], ast.returnType))

