
"""
 * @author nhphung
"""
#1927029

from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
class FloatType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    eletype: Type

# @dataclass
# class MType:
#     intype:List[Type]
#     restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

@dataclass
class MType:
    intype:List[Symbol]
    restype:Type

class StaticChecker(BaseVisitor,Utils):
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("int_of_float",MType([Symbol('abc', FloatType())],IntType())),
Symbol("float_of_int",MType([Symbol('abc', IntType())],FloatType())),
Symbol("int_of_string",MType([Symbol('abc', StringType())],IntType())),
Symbol("string_of_int",MType([Symbol('abc', IntType())],StringType())),
Symbol("float_of_string",MType([Symbol('abc', StringType())],FloatType())),
Symbol("string_of_float",MType([Symbol('abc', FloatType())],StringType())),
Symbol("bool_of_string",MType([Symbol('abc', StringType())],BoolType())),
Symbol("string_of_bool",MType([Symbol('abc', BoolType())],StringType())),
Symbol("read",MType([],StringType())),
Symbol("printLn",MType([],VoidType())),
Symbol("printStr",MType([Symbol('abc', StringType())],VoidType())),
Symbol("printStrLn",MType([Symbol('abc', StringType())],VoidType()))]                           
    
    def check(self):
        return self.visit(self.ast,self.global_envi)
    # acc listfunction, i is function
    def breadthVisit(self, acc, i):
        funcName = i.name.name
        lookupFunctionName = self.lookup(funcName, acc, lambda x: x.name)
        if(lookupFunctionName):
            raise Redeclared(Function(), funcName)

        listParam = []
 
        try:
            listParam = reduce(lambda acc, i: self.visit(i, acc), i.param, listParam)
        except Redeclared as error:
            raise Redeclared(Parameter(), error.n)
 
        return acc + [Symbol(funcName, MType(listParam, Unknown()))]

    # class FuncDecl(Decl):
    # name: Id
    # param: List[VarDecl]
    # body: Tuple[List[VarDecl],List[Stmt]]

    def visitProgram(self,ast, c):

        varDecl = list(filter(lambda i: type(i) is VarDecl, ast.decl))
        c = reduce(lambda acc, x: self.visit(x, acc), varDecl, c)

        funcDecl = list(filter(lambda i: type(i) is FuncDecl, ast.decl))
        c = reduce(self.breadthVisit, funcDecl, c)

        [self.visit(x, c) for x in funcDecl]

    def visitVarDecl(self, ast, c):
        varName = ast.variable.name

        if self.lookup(varName, c, lambda x: x.name):
            raise Redeclared(Variable(), varName)

        if(ast.varInit):
            typeVar = self.visit(ast.varInit, c)
        else: 
            typeVar = Unknown()

        if ast.varDimen:
            return c + [Symbol(varName, ArrayType(ast.varDimen, typeVar))]

        return c + [Symbol(varName,typeVar)]

    def visitFuncDecl(self, ast, c):
       
        lookupFunctionName = self.lookup(ast.name.name, c, lambda x: x.name) 
        pa = lookupFunctionName.mtype.intype #List[Symbol] of params

        pa = reduce(lambda acc, x: self.visit(x, acc), ast.body[0], pa)
        [self.visit(x, (pa + c, VoidType(), lookupFunctionName)) for x in ast.body[1]] 


    def visitAssign(self, ast, c):
        try:
            lhs = self.visit(ast.lhs, (c[0], Unknown())) 
            rhs = self.visit(ast.rhs, (c[0], lhs))
            lhs = self.visit(ast.lhs, (c[0], rhs))
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        
        if type(lhs) is VoidType:
            raise TypeMismatchInStatement(ast)

        if type(lhs) is not type(rhs):
            raise TypeMismatchInStatement(ast)

        if type(lhs) is Unknown or (type(lhs) is ArrayType and type(lhs.eletype) is Unknown):
            raise TypeCannotBeInferred(ast)

    def visitBinaryOp(self, ast, c):
        op = ast.op
        opInt = ['+', '-', '*', '\\', '%', '==', '!=', '<', '>', '<=', '>=']
        opIntBool = ['==', '!=', '<', '>', '<=', '>=']
        opFloat = ['+.', '-.', '*.', '/', '=/=', '<.', '>.', '<=.', '>=.']
        opFloatBool = ['=/=', '<.', '>.', '<=.', '>=.']
        if (op in opInt):
            leftType = self.visit(ast.left, (c[0], IntType()))
            rightType = self.visit(ast.right, (c[0], IntType()))
            if (type(leftType) is IntType and type(rightType) is IntType):
                if (op in opIntBool):
                    return BoolType()
                return IntType()

            raise TypeMismatchInExpression(ast)
        if (op in opFloat):
            leftType = self.visit(ast.left, (c[0], FloatType()))
            rightType = self.visit(ast.right, (c[0], FloatType()))

            if (type(leftType) is FloatType and type(rightType) is FloatType):
                if (op in opFloatBool):
                    return BoolType()
                return FloatType()

            raise TypeMismatchInExpression(ast)

    # class UnaryOp(Expr):
    # op:str
    # body:Expr

    def visitUnaryOp(self, ast, c):
        op = ast.op

        if (op == "-"):
            bodyType = self.visit(ast.body, (c[0], IntType()))

            if (type(bodyType) is IntType):
                return IntType()

        if (op == '-.'):
            bodyType = self.visit(ast.body, (c[0], FloatType()))

            if (type(bodyType) is FloatType):
                return FloatType()

        if (op == '!'):
            bodyType = self.visit(ast.body, (c[0], BoolType()))

            if (type(bodyType) is BoolType):
                return BoolType()

        raise TypeMismatchInExpression(ast)

    # class ArrayCell(LHS):
    # arr:Id
    # idx:List[Expr]
    def visitArrayCell(self, ast, c):
        arrName = ast.arr.name
        arr = self.lookup(arrName, c[0], lambda x: x.name)
        if (arr is None):
            raise Undeclared(Identifier(), arrName)
        if(len(arr.mtype.dimen) is not len(ast.idx)):
            raise TypeMismatchInExpression(ast)
        for i in ast.idx:
            idxType = self.visit(i, (c[0], IntType()))
            if (type(idxType) is not IntType):
                raise TypeMismatchInExpression(ast)

        if type(arr.mtype.eletype) is Unknown and type(c[1]) not in [Unknown, ArrayType]:
            arr.mtype.eletype = c[1]
        
        return arr.mtype.eletype

    # class CallExpr(Expr):
    # method:Id
    # param:List[Expr]
        
    def visitCallExpr(self, ast, c):
        functionName = ast.method.name
        functionType = self.lookup(functionName, c[0], lambda x: x.name) 
        if not functionType:
            raise Undeclared(Function(), functionName)

        funcMtype = functionType.mtype

        if type(funcMtype) is not MType:
            raise TypeMismatchInExpression(ast)

        funcIntype = funcMtype.intype 

        if(len(funcIntype) is not len(ast.param)):
            raise TypeMismatchInExpression(ast)

        for index in range(len(funcIntype)):
            paramType = funcIntype[index]
            referType = self.visit(ast.param[index], (c[0], paramType.mtype))

            if type(referType) is ArrayType:
                if (type(paramType.mtype) is ArrayType and type(paramType.mtype.eletype) is Unknown):
                    paramType.mtype.eletype = referType.eletype
            elif type(referType) is not Unknown:
                if type(paramType.mtype) is Unknown:
                    paramType.mtype = referType

            if ((type(paramType.mtype) is Unknown) or (type(paramType.mtype) is ArrayType and type(paramType.mtype.eletype) is Unknown)):
                raise TypeCannotBeInferred(ast)

            if type(paramType.mtype) is not type(referType):
                raise TypeMismatchInExpression(ast.param[index])

        if (type(funcMtype.restype) is Unknown and type(c[1]) is not Unknown):
            funcMtype.restype = c[1]

        if type(funcMtype.restype) is Unknown:
            raise TypeCannotBeInferred(ast)

        return funcMtype.restype

    # class CallStmt(Stmt):
    # method:Id
    # param:List[Expr]
    def visitCallStmt(self, ast, c):
        try:
            # CallStmtType = self.callExpr(ast, (c[0], VoidType(), c[2]))
            CallStmtType = self.visitCallExpr(ast, (c[0], VoidType(), c[2]))
            if type(CallStmtType) is not VoidType:
                raise TypeMismatchInStatement(ast)
        except TypeMismatchInExpression as error:
            if error.exp is ast:
                raise TypeMismatchInStatement(ast)
            else:
                raise TypeMismatchInExpression(error.exp)


    # class If(Stmt):
    # ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
    # elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
    def visitIf(self, ast, c):
        for ifthenStmt in ast.ifthenStmt:
            try:
                expr = self.visit(ifthenStmt[0], (c[0], BoolType()))
            except TypeCannotBeInferred:
                raise TypeCannotBeInferred(ast)
            if (type(expr) is not BoolType):
                raise TypeMismatchInStatement(ast)
            varLocal = []
            varLocal = reduce(lambda acc, x: self.visit(x, acc), ifthenStmt[1], varLocal)
            [self.visit(x, (varLocal + c[0], VoidType(), c[2])) for x in ifthenStmt[2]]

        elseStmt = reduce(lambda acc, i: self.visit(i, acc), ast.elseStmt[0], [])
        [self.visit(i, (elseStmt + c[0], Unknown())) for i in ast.elseStmt[1]]

        
    # class While(Stmt):
    # exp: Expr
    # sl:Tuple[List[VarDecl],List[Stmt]]
    def visitWhile(self, ast, c):
        try:
            expr = self.visit(ast.exp, (c[0], BoolType()))
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        if type(expr) is not BoolType:
            raise TypeMismatchInStatement(ast)

        varLocal = []
        varLocal = reduce(lambda acc, x: self.visit(x, acc), ast.sl[0], varLocal)
        [self.visit(x, (varLocal + c[0], VoidType(), c[2])) for x in ast.sl[1]]

    # class Dowhile(Stmt):
    # sl:Tuple[List[VarDecl],List[Stmt]]
    # exp: Expr
    def visitDowhile(self, ast, c):
        try:
            expr = self.visit(ast.exp, (c[0], BoolType()))
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        if type(expr) is not BoolType:
            raise TypeMismatchInStatement(ast)

        varLocal = []
        varLocal = reduce(lambda acc, x: self.visit(x, acc), ast.sl[0], varLocal)
        [self.visit(x, (varLocal + c[0], VoidType(), c[2])) for x in ast.sl[1]]

    # class For(Stmt):
    # idx1: Id
    # expr1:Expr
    # expr2:Expr boolType
    # idx2: Id
    # expr3:Expr
    # loop: Tuple[List[VarDecl],List[Stmt]]
    def visitFor(self, ast, c):
        try:
            e1 = self.visit(ast.idx1, (c[0], IntType()))
            e2 = self.visit(ast.expr1, (c[0], IntType()))
            e3 = self.visit(ast.expr2, (c[0], BoolType()))
            e4 = self.visit(ast.idx2, (c[0], IntType()))
            e5 = self.visit(ast.expr3, (c[0], IntType()))
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        if type(e1) is not IntType:
            raise TypeMismatchInStatement(ast)

        if type(e2) is not IntType:
            raise TypeMismatchInStatement(ast)

        if type(e3) is not BoolType:
            raise TypeMismatchInStatement(ast)

        if type(e4) is not IntType:
            raise TypeMismatchInStatement(ast)

        if type(e5) is not IntType:
            raise TypeMismatchInStatement(ast)

        varLocal = []
        varLocal = reduce(lambda acc, x: self.visit(x, acc), ast.loop[0], varLocal)
        [self.visit(x, (varLocal + c[0], VoidType(), c[2])) for x in ast.loop[1]]


    # class Return(Stmt):
    # expr:Expr # None if no expression
    def visitReturn(self, ast, c):
        reType = VoidType() 

        if ast.expr:
            try:
                reType = self.visit(ast.expr, (c[0], Unknown()))
            except TypeCannotBeInferred:
                raise TypeCannotBeInferred(ast)

        if type(reType) is Unknown:
            raise TypeCannotBeInferred(ast)

        if type(c[2].mtype.restype) is Unknown:
            c[2].mtype.restype = reType

        if type(c[2].mtype.restype) is not type(reType):
            raise TypeMismatchInStatement(ast)

    def visitId(self, ast, c):
        idName = ast.name
        typeId = self.lookup(idName, c[0], lambda x: x.name)
        if typeId == None:
            raise Undeclared(Identifier(), idName)

        if type(typeId.mtype) is Unknown and type(c[1]) is not Unknown and type(c[1]) is not ArrayType:
            typeId.mtype = c[1]

        return typeId.mtype

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()