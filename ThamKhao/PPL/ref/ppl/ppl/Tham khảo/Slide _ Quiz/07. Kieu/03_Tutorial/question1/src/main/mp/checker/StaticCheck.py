
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class FunctionType(Type):
    def __init__(self, list_input, output):
        self.list_input = list_input
        self.output = output
    def accept(self, v, param):
        return v.visitFunctionType(self, param)


class StaticChecker(BaseVisitor, Utils):

    global_envi = [Symbol("getInt", MType([], IntType())),
                   Symbol("putIntLn", MType([IntType()], VoidType()))]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def typeCheck(self,lhs,rhs):
        if type(lhs) is IntType and type(rhs) is IntType:
            return True
        elif type(lhs) is FloatType and type(rhs) is FloatType:
            return True
        elif type(lhs) is StringType and type(rhs) is StringType:
            return True
        elif type(lhs) is VoidType and type(rhs) is VoidType:
            return True
        elif type(lhs) is BoolType and type(rhs) is BoolType:
            return True
        elif type(lhs) is ArrayType and type(rhs) is ArrayType:
            return self.typeCheck(lhs.eleType,rhs.eleType) and int(lhs.lower) ==int(rhs.lower) and int(lhs.upper) ==int(rhs.upper)
        elif type(lhs) is FunctionType and type(rhs) is FunctionType:
            if len(lhs.list_input) != len(rhs.list_input):
                return False
            elif not (self.typeCheck(lhs.output,rhs.output)):
                return False
            elif len(lhs.list_input)==0 and len(rhs.list_input)==0:
                return True
            else:
                lhs_rhs = list(zip(lhs.list_input,rhs.list_input))
                for x in lhs_rhs:
                    if not self.typeCheck(x[0],x[1]):
                        return False                    
            return True 
        else:
            return False

    def visitProgram(self, ast, c):
        return [self.visit(x, c) for x in ast.decl]

    def visitFuncDecl(self, ast, c):
        return list(map(lambda x: self.visit(x, (c, True)), ast.body))

    def visitCallStmt(self, ast, c):
        at = [self.visit(x, (c[0], False)) for x in ast.param]

        res = self.lookup(ast.method.name, c[0], lambda x: x.name)
        if res is None or not type(res.mtype) is MType or not type(res.mtype.rettype) is VoidType:
            raise Undeclared(Procedure(), ast.method.name)
        elif len(res.mtype.partype) != len(at):
            raise TypeMismatchInStatement(ast)
        else:
            return res.mtype.rettype

    def visitIntLiteral(self, ast, c):
        return IntType()
    
