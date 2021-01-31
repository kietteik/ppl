'''
@student    Nguyễn Tuấn Kiệt
@mssv       1927021
'''
"""
 * @author nhphung
"""




from functools import *
from StaticError import *
from Visitor import *
from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import *
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
    dimen: List[int]
    eletype: Type


@dataclass
class MType:
    intype: List[Type]
    restype: Type

@dataclass
class Symbol:
    name: str
    mtype: Type

class StaticChecker(BaseVisitor):
    def __init__(self, ast):
        self.ast = ast
        self.global_envi = [
            Symbol("int_of_float", MType(
                [Symbol('abc', FloatType())], IntType())),
            Symbol("float_of_int", MType(
                [Symbol('abc', IntType())], FloatType())),
            Symbol("int_of_string", MType(
                [Symbol('abc', StringType())], IntType())),
            Symbol("string_of_int", MType(
                [Symbol('abc', IntType())], StringType())),
            Symbol("float_of_string", MType(
                [Symbol('abc', StringType())], FloatType())),
            Symbol("string_of_float", MType(
                [Symbol('abc', FloatType())], StringType())),
            Symbol("bool_of_string", MType(
                [Symbol('abc', StringType())], BoolType())),
            Symbol("string_of_bool", MType(
                [Symbol('abc', BoolType())], StringType())),
            Symbol("read", MType([], StringType())),
            Symbol("printLn", MType([], VoidType())),
            Symbol("printStr", MType(
                [Symbol('abc', StringType())], VoidType())),
            Symbol("printStrLn", MType([Symbol('abc', StringType())], VoidType()))]

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def funcNameCollective(self, ast, c):
        for i in self.global_envi:
            c[i.name] = i
        name = ast.name.name
        if name in c.keys():
            raise Redeclared(Function(), name)
        params = {}
        try:
            [self.visit(x, params) for x in ast.param]
            paramsList = list(params.values())
        except Redeclared as e:
            raise Redeclared(Parameter(), e.n)
        c[name] = Symbol(name, MType(paramsList, Unknown()))

    # decl : List[Decl]
    def visitProgram(self, ast, c):
        c = {}
        varDec = list(filter(lambda x: type(x) == VarDecl, ast.decl))
        funcDec = list(filter(lambda x: type(x) == FuncDecl, ast.decl))
        [self.visit(x, c) for x in varDec]
        [self.funcNameCollective(x, c) for x in funcDec]
        if 'main' not in c or type(c['main'].mtype) != MType:
            raise NoEntryPoint(ast)
        [self.visit(x, c) for x in funcDec]

    # variable : Id
    # varDimen : List[int] # empty list for scalar variable
    # varInit  : Literal   # null if no initial
    def visitVarDecl(self, ast, c):
        name = ast.variable.name
        if name in c:
            raise Redeclared(Variable(), name)
        if ast.varInit:
            typeInit = self.visit(ast.varInit, c)
            # if type(typeInit)==ArrayType and len(ast.varDimen) != len(typeInit.dimen):
            #     raise TypeMismatchInExpression(ast)
        elif ast.varDimen:
            typeInit = ArrayType(ast.varDimen, Unknown())
        else:
            typeInit = Unknown()
        
        c[name] = Symbol(name, typeInit)

    # name: Id
    # param: List[VarDecl]
    # body: Tuple[List[VarDecl],List[Stmt]]
    def visitFuncDecl(self, ast, c):
        
        params = c[ast.name.name].mtype.intype                  # get params dec
        localVar = {}
        for sym in params:
            localVar[sym.name] = sym
        [self.visit(x, localVar) for x in ast.body[0]]          # get var dec
        canUserVar = c.copy()
        canUserVar.update(localVar)
        
        [self.visit(x, (canUserVar, VoidType(), c[ast.name.name]))
         for x in ast.body[1]]
        if type(c[ast.name.name].mtype.restype) == Unknown:
            hasReturn =0
            for i in ast.body[1]:
                if type(i)== Return and i.expr!=None:
                    hasReturn=1
            if hasReturn==0:
                c[ast.name.name].mtype.restype = VoidType()
        
    # lhs: LHS
    # rhs: Expr
    def visitAssign(self, ast, c):
        try:
            left = self.visit(ast.lhs, (c[0], Unknown()))
            right = self.visit(ast.rhs, (c[0], left))
            left = self.visit(ast.lhs, (c[0], right))
        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        except TypeMismatchInStatement:
            raise TypeMismatchInStatement(ast)

        if type(left) is VoidType:
            raise TypeMismatchInStatement(ast)
        if type(left) is not type(right):
            raise TypeMismatchInStatement(ast)
        if type(left) is Unknown or (type(left) is ArrayType and type(left.eletype) is Unknown):
            raise TypeCannotBeInferred(ast)

    # op:str
    # left:Expr
    # right:Expr
    def visitBinaryOp(self, ast, c):
        op = ast.op
        opFloat = ['+.', '-.', '*.', '/', '=/=', '<.', '>.', '<=.', '>=.']
        opFloatBool = ['=/=', '<.', '>.', '<=.', '>=.']
        opBool = ['&&','||']
        opInt = ['+', '-', '*', '\\', '%', '==', '!=', '<', '>', '<=', '>=']
        opIntBool = ['==', '!=', '<', '>', '<=', '>=']

        if op in opBool:
            leftType = self.visit(ast.left, (c[0], BoolType()))
            rightType = self.visit(ast.right, (c[0], BoolType()))
            if (type(leftType) is BoolType and type(rightType) is BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)
        if op in opInt:
            leftType = self.visit(ast.left, (c[0], IntType()))
            rightType = self.visit(ast.right, (c[0], IntType()))
            if (type(leftType) is IntType and type(rightType) is IntType):
                if (op in opIntBool):
                    return BoolType()
                return IntType()
            raise TypeMismatchInExpression(ast)
        if op in opFloat:
            leftType = self.visit(ast.left, (c[0], FloatType()))
            rightType = self.visit(ast.right, (c[0], FloatType()))

            if (type(leftType) is FloatType and type(rightType) is FloatType):
                if (op in opFloatBool):
                    return BoolType()
                return FloatType()
            raise TypeMismatchInExpression(ast)
        

    # op:str
    # body:Expr
    def visitUnaryOp(self, ast, c):
        if ast.op == '!':
            bodyType = self.visit(ast.body, (c[0], BoolType()))
            if (type(bodyType) is BoolType):
                return BoolType()
        if ast.op == "-":
            bodyType = self.visit(ast.body, (c[0], IntType()))
            if (type(bodyType) is IntType):
                return IntType()
        if ast.op == '-.':
            bodyType = self.visit(ast.body, (c[0], FloatType()))
            if (type(bodyType) is FloatType):
                return FloatType()
        raise TypeMismatchInExpression(ast)

    # arr:Expr  Id or FunctionCall
    # idx:List[Expr]
    def visitArrayCell(self, ast, c):
        arrType = self.visit(ast.arr, (c[0], ArrayType([0]*len(ast.idx), c[1])))
        if type(arrType) != ArrayType:
            raise TypeMismatchInExpression(ast)
        if len(arrType.dimen) != len(ast.idx):
            raise TypeMismatchInExpression(ast)
        for i in ast.idx:
            idxType = self.visit(i, (c[0], IntType()))
            if type(idxType) != IntType:
                raise TypeMismatchInExpression(ast)
        if type(arrType.eletype) is Unknown and type(c[1]) not in [Unknown, ArrayType]:
            arrType.eletype = c[1]
        
        return arrType.eletype
        

    # method:Id
    # param:List[Expr]
    def visitCallExpr(self, ast, c):
        funcName = ast.method.name
        if funcName not in c[0]:
            raise Undeclared(Function(), funcName)
        funcMtype = c[0][funcName].mtype
        if type(funcMtype) is not MType:
            raise Undeclared(Function(), funcName)
        funcIntype = funcMtype.intype
        if(len(funcIntype) is not len(ast.param)):
            raise TypeMismatchInExpression(ast)

        for i in range(len(funcIntype)):
            paramType = funcIntype[i]
            argType = self.visit(ast.param[i], (c[0], paramType.mtype))

            if type(argType) is ArrayType:
                if type(paramType.mtype) is not ArrayType:
                    raise TypeMismatchInExpression(ast)
                if (type(paramType.mtype) is ArrayType and type(paramType.mtype.eletype) is Unknown):
                    paramType.mtype.eletype = argType.eletype
                elif (type(paramType.mtype) is ArrayType and type(argType.eletype) is Unknown):
                    argType.eletype = paramType.mtype.eletype
                elif (type(paramType.mtype) is ArrayType and type(argType.eletype) != type(paramType.mtype.eletype)):
                    raise TypeMismatchInExpression(ast)

            if type(argType) is not Unknown:
                if type(paramType.mtype) is Unknown:
                    paramType.mtype = argType
            elif type(paramType.mtype) not in [ArrayType, Unknown]:
                argType = paramType.mtype

            if type(paramType.mtype) is not type(argType):
                raise TypeMismatchInExpression(ast)

            if ((type(paramType.mtype) is Unknown) or (type(paramType.mtype) is ArrayType and type(paramType.mtype.eletype) is Unknown)):
                raise TypeCannotBeInferred(ast)

        if (type(funcMtype.restype) is Unknown and type(c[1]) is not Unknown):
            funcMtype.restype = c[1]
        if type(funcMtype.restype) is Unknown:
            raise TypeCannotBeInferred(ast)

        return funcMtype.restype

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

    # """Expr is the condition,
    #     List[VarDecl] is the list of declaration in the beginning of Then branch, empty list if no declaration
    #     List[Stmt] is the list of statement after the declaration in Then branch, empty list if no statement
    # """
    # ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
    # elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
    def visitIf(self, ast, c):
        for ifthenStmt in ast.ifthenStmt:
            try:
                expr = self.visit(ifthenStmt[0], (c[0], BoolType()))
            except TypeCannotBeInferred:
                raise TypeCannotBeInferred(ast)
            except TypeMismatchInStatement:
                raise TypeMismatchInStatement(ast)

            if (type(expr) != BoolType):
                raise TypeMismatchInStatement(ast)
            localVar = {}
            [self.visit(x, localVar) for x in ifthenStmt[1]]
            canUseVar = c[0].copy()
            canUseVar.update(localVar)
            [self.visit(x, (canUseVar, VoidType(), c[2]))
             for x in ifthenStmt[2]]

        localVar = {}
        [self.visit(x, localVar) for x in ast.elseStmt[0]]
        canUseVar = c[0].copy()
        canUseVar.update(localVar)
        [self.visit(i, (canUseVar, VoidType(), c[2])) for i in ast.elseStmt[1]]

    # idx1: Id
    # expr1:Expr    Int
    # expr2:Expr    Bool
    # expr3:Expr    Int
    # loop: Tuple[List[VarDecl],List[Stmt]]
    def visitFor(self, ast, c):
        try:
            idx1 = self.visit(ast.idx1, (c[0], IntType()))
            exp1 = self.visit(ast.expr1, (c[0], IntType()))
            exp2 = self.visit(ast.expr2, (c[0], BoolType()))
            exp3 = self.visit(ast.expr3, (c[0], IntType()))

        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        except TypeMismatchInStatement:
            raise TypeMismatchInStatement(ast)

        if any([type(idx1) != IntType, type(exp1) != IntType, type(exp2) != BoolType, type(exp3) != IntType]):
            raise TypeMismatchInStatement(ast)

        localVar = {}
        [self.visit(x, localVar) for x in ast.loop[0]]
        canUseVar = c[0].copy()
        canUseVar.update(localVar)
        [self.visit(x, (canUseVar, VoidType(), c[2])) for x in ast.loop[1]]


    # exp: Expr
    # sl:Tuple[List[VarDecl],List[Stmt]]
    def visitWhile(self, ast, c):
        try:
            exp = self.visit(ast.exp, (c[0], BoolType()))

        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)
        except TypeMismatchInStatement:
            raise TypeMismatchInStatement(ast)

        if type(exp) != BoolType:
            raise TypeMismatchInStatement(ast)
        localVar = {}
        [self.visit(x, localVar) for x in ast.sl[0]]
        canUseVar = c[0].copy()
        canUseVar.update(localVar)
        [self.visit(x, (canUseVar, VoidType(), c[2])) for x in ast.sl[1]]

    # sl:Tuple[List[VarDecl],List[Stmt]]
    # exp: Expr
    def visitDowhile(self, ast, c):
        try:
            exp = self.visit(ast.exp, (c[0], BoolType()))

        except TypeCannotBeInferred:
            raise TypeCannotBeInferred(ast)

        except TypeMismatchInStatement:
            raise TypeMismatchInStatement(ast)

        if type(exp) != BoolType:
            raise TypeMismatchInStatement(ast)
        localVar = {}
        [self.visit(x, localVar) for x in ast.sl[0]]
        canUseVar = c[0].copy()
        canUseVar.update(localVar)
        [self.visit(x, (canUseVar, VoidType(), c[2])) for x in ast.sl[1]]

    # expr:Expr # None if no expression
    def visitReturn(self, ast, c):
        returnType = VoidType()
        if ast.expr:
            try:
                returnType = self.visit(ast.expr, (c[0], Unknown()))
            except TypeCannotBeInferred:
                raise TypeCannotBeInferred(ast)

        if type(returnType) == Unknown and type(c[2].mtype.restype) == Unknown:
            raise TypeCannotBeInferred(ast)

        if type(returnType) == Unknown:
            returnType = c[2].mtype.restype

        if type(c[2].mtype.restype) == Unknown:
            c[2].mtype.restype = returnType
        if type(c[2].mtype.restype) != type(returnType):
            raise TypeMismatchInStatement(ast)

        if type(returnType) == ArrayType:
            if len(returnType.dimen) != len(c[2].mtype.restype.dimen):
                raise TypeMismatchInStatement(ast)
            if type(returnType.eletype) == Unknown:
                returnType.eletype = c[2].mtype.restype.eletype
            if type(c[2].mtype.restype.eletype) == Unknown:
                c[2].mtype.restype.eletype =returnType.eletype 
            if type(returnType.eletype) != type(c[2].mtype.restype.eletype):
                raise TypeMismatchInStatement(ast)
            if type(returnType.eletype) == Unknown:
                raise TypeCannotBeInferred(ast)
        

    def visitId(self, ast, c):
        name = ast.name
        if name not in c[0]:
            raise Undeclared(Identifier(), name)

        idType = c[0][name]
        if type(c[0][name].mtype) == Unknown and type(c[1]) != Unknown and type(c[1]) != ArrayType:
            c[0][name].mtype = c[1]

        elif type(idType.mtype) == ArrayType and type(c[1]) == ArrayType:
            # if len(idType.mtype.dimen) != len(c[1].dimen):
            #     raise TypeMismatchInExpression(ast)
            # if type(idType.mtype.eletype) == type(c[1].eletype) and type(idType.mtype.eletype) == Unknown:
            #     raise TypeCannotBeInferred(ast)
            if type(idType.mtype.eletype) == Unknown:
                c[0][name].mtype.eletype = c[1].eletype
            elif type(c[1].eletype) == Unknown:
                c[1].eletype = idType.mtype.eletype

        return idType.mtype

    # value:List[Literal]
    def visitArrayLiteral(self, ast, c):
        dim = []
        eleType = Unknown()
        arr = ast.value
        while True:
            getDim = len(arr)
            dim += [getDim]
            arr = arr[0].value
            if type(arr) != list:
                eleType = type(arr)
                break
        if eleType == int:
            eleType = IntType()
        elif eleType == str:
            eleType = StringType()
        elif eleType == float:
            eleType = FloatType()
        else:
            eleType = BoolType()

        return ArrayType(dim, eleType)

    # value:int
    def visitIntLiteral(self, ast, c):
        return IntType()

    # value:float
    def visitFloatLiteral(self, ast, c):
        return FloatType()

    # value:bool
    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    # value:str
    def visitStringLiteral(self, ast, c):
        return StringType()

    
