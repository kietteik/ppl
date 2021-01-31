
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
import itertools

import sys
sys.path.append('../../../../target/main/mp/parser')
sys.path.append('../utils')

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor, Utils):

    global_envi = [Symbol("getInt", MType([], IntType())),
                   Symbol("putInt", MType([IntType()], VoidType())),
                   Symbol("putIntLn", MType([IntType()], VoidType())),
                   Symbol("getFloat", MType([], FloatType())),
                   Symbol("putFloat", MType([FloatType()], VoidType())),
                   Symbol("putFloatLn", MType([FloatType()], VoidType())),
                   Symbol("putBool", MType([BoolType()], VoidType())),
                   Symbol("putBoolLn", MType([BoolType()], VoidType())),
                   Symbol("putString", MType([StringType()], VoidType())),
                   Symbol("putStringLn", MType([StringType()], VoidType())),
                   Symbol("putLn", MType([], VoidType()))
                   ]

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    def flatten(self, lst):
        flatten_lst = []
        for i in lst:
            if not isinstance(i,list):
                flatten_lst.append(i)
            else:
                for j in i:
                    flatten_lst.append(j)
        return flatten_lst

    def raiseRedeclared(self, kind, symbol, list_check):
        checkName = self.lookup(symbol.name, list_check, lambda x: x.name)
        if checkName is not None:
            raise Redeclared(kind, symbol.name)
        return symbol

    def typeCheck(self,lhs,rhs):
        if type(lhs) is type(rhs) and type(lhs) in [IntType, BoolType]:
            return lhs
        elif type(lhs) is FloatType and type(rhs) in [FloatType, IntType]:
            return FloatType()
        if type(lhs) is StringType and type(rhs) is StringType:
            return StringType()
        if type(lhs) is ArrayType and type(rhs) is ArrayType:
            if (int(lhs) == int(rhs)) and (int(lhs) == int(rhs)) and (type(lhs.eleType) == type(rhs.eleType)):
                return lhs
        return None

    def checkBlockReturn(self, stmt): # For FuncDecl
        if type(stmt) is Return:
            return 1
        if type(stmt) is Block:
            for x in stmt.member: # stmt.member -> [Stmt: Block, VarDecl]
                if type(x) is not VarDecl:
                    return self.checkBlockReturn(x)  # Stmt
        if type(stmt) is If and type(stmt.elseStmt) is not None:
            return self.checkBlockReturn(stmt.thenStmt) * self.checkBlockReturn(stmt.elseStmt) # Both stmts have 'Return' -> return 1
        return 0

    def checkReachableFunction(self, lst_global, lst_callExpr):
        lst = [i.name for i in filter(lambda x: True if type(x.mtype) is MType else False, lst_callExpr)]
        for x in filter(lambda x: True if type(x.mtype) is MType else False, lst_global):
            if x.name not in lst + ["main"] and x.name not in [i.name for i in StaticChecker.global_envi]:
                raise UnreachableFunction(x.name)   
        return None

    ####################################        VISIT FUNCTION      #####################################################

    def visitProgram(self, ast, c):
        env = c.copy()
        self.lst_callExpr = [] # For unreachable function
        # Check Redeclared for VarDecl and FuncDecl
        for decl in ast.decl:
            if type(decl) is VarDecl:  # Variable declaration
                env.append(self.raiseRedeclared(Variable(), Symbol(decl.variable, decl.varType), env))
            else:  # Function declaration
                lstTypePara = [x.varType for x in decl.param]
                env.append(self.raiseRedeclared(Function(), Symbol(decl.name.name, MType(lstTypePara, decl.returnType)), env))
        # Check 'main' function
        main = self.lookup("main", env, lambda x: x.name)
        if (main is None) or (type(main.mtype) is not MType): # No name "main" or not func
            raise NoEntryPoint()
        # Visit 'decl' with 'env'
        visitDecl = [self.visit(x, env) for x in ast.decl]
        self.checkReachableFunction(env, self.lst_callExpr)


    def visitVarDecl(self, ast, c):
        return Symbol(ast.variable, ast.varType)


    def visitFuncDecl(self, ast, c):
        local_env = [] # For VarDecl Parameter and Local Environment
        for varDecl_para in ast.param: 
            local_env.append(self.raiseRedeclared(Parameter(), Symbol(varDecl_para.variable, varDecl_para.varType), local_env))
        # Check Func not Return
        if (type(ast.returnType) is not VoidType):
            # Check each Stmt
            flag = 0
            for x in ast.body.member: # [Stmt, VarDecl]
                if x is not VarDecl: # x -> Stmt
                    flag = flag + self.checkBlockReturn(x)  
            if flag == 0:
                raise FunctionNotReturn(ast.name.name) 
        # Visit Body (Block)
        # c[0]: VarDecl_Para, c[1]: outer env (global), c[2]: Continue/Break, c[3]: for visitReturn()
        para_env = local_env.copy()
        for blockMember in ast.body.member: # member: [Stmt: Block, VarDecl]
            if type(blockMember) is VarDecl:  # Variable declaration
                local_env.append(self.raiseRedeclared(Variable(), Symbol(blockMember.variable, blockMember.varType), local_env))
            else: self.visit(blockMember, (para_env, local_env + c, False, ast.returnType))


    def visitBlock(self, ast, c): # member: [Stmt: Block, VarDecl]
        local_env = c[0].copy() # c[0]: Null or VarDecl_Para
        for member in ast.member:
            if type(member) is VarDecl:  # Variable declaration
                local_env.append(self.raiseRedeclared(Variable(), Symbol(member.variable, member.varType), local_env))
            else: self.visit(member, (c[0], local_env + c[1], c[2], c[3]))


    def visitReturn(self, ast, c):
        flag = False
        retExp = self.visit(ast.expr, c) if ast.expr is not None else None
        if retExp is None and type(c[3]) is VoidType:
            flag = True
        elif type(retExp) in [ArrayType, ArrayPointerType] and type(retExp.eleType) is type(c[3].eleType):
            flag = True
        elif type(retExp) is type(c[3]) and not (type(retExp) in [ArrayType, ArrayPointerType]):
            flag = True
        elif type(retExp) is IntType and type(c[3]) is FloatType:
            flag = True
        if flag == False:
            raise TypeMismatchInStatement(ast)
        return retExp


    def visitIf(self, ast, c):
        if_Exp = self.visit(ast.expr, c)
        if type(if_Exp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        if_thenStmt = self.visit(ast.thenStmt, c)
        if ast.elseStmt:
            if_elsestmt = self.visit(ast.elseStmt, c)


    def visitFor(self, ast, c):
        for_Expr1 = self.visit(ast.expr1, c)
        for_Expr2 = self.visit(ast.expr2, c)
        for_Expr3 = self.visit(ast.expr3, c)
        if type(for_Expr1) is not IntType or type(for_Expr3) is not IntType or type(for_Expr2) is not BoolType:
            raise TypeMismatchInStatement(ast)
        visitLoopStmt = self.visit(ast.loop, (c[0], c[1], True, c[3]))


    def visitDowhile(self, ast, c):
        dowhile_Stmts = [self.visit(x, (c[0], c[1], True, c[3])) for x in ast.sl]
        dowhile_Exp = self.visit(ast.exp, c)
        if type(dowhile_Exp) is not BoolType:
            raise TypeMismatchInStatement(ast)
        

    def visitContinue(self, ast, c):
        if not c[2]:
            raise ContinueNotInLoop()


    def visitBreak(self, ast, c):
        if not c[2]:
            raise BreakNotInLoop()


    def visitCallExpr(self, ast, c):
        lst_paraCall = [self.visit(x, c) for x in ast.param]
        lst = self.flatten(c[0] + c[1])
        res = self.lookup(ast.method.name, lst, lambda x: x.name)
        # Check Undeclared Func
        if res is None or type(res.mtype) is not MType:
            raise Undeclared(Function(),ast.method.name)
        # Match Parameter
        elif True in [type(x) in [ArrayType, ArrayPointerType] for x in res.mtype.partype]:
            for a, b in zip(lst_paraCall, res.mtype.partype):
                if type(a) in [ArrayType, ArrayPointerType]: 
                    if type(a.eleType) is not type(b.eleType):
                        raise TypeMismatchInExpression(ast)
        elif len(res.mtype.partype) != len(lst_paraCall) or True in [(type(a) != type(b) and not (type(a) is IntType and type(b) is FloatType)) for a, b in zip(lst_paraCall, res.mtype.partype)]:
            raise TypeMismatchInExpression(ast)
        # For Unreachable Function
        self.lst_callExpr.append(res)
        return res.mtype.rettype


    def visitBinaryOp(self,ast,c):    
        left = self.visit(ast.left,c)
        right = self.visit(ast.right,c)

        if (ast.op in ['&&', '||']):
            if type(left) is BoolType and type(right) is BoolType:
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)
        if (ast.op in ['==','!=']):
            if type(left) == type(right):
                if (left in [BoolType(), IntType()]):
                    return BoolType()
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
        if (ast.op in ['<', '<=', '>', '>=']):
            if(type(left) in [IntType, FloatType]) and (type(right) in [IntType, FloatType]):
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)       
        if (ast.op in ['+', '-', '*', '/']):
            if (type(left) in [IntType, FloatType]) and (type(right) in [IntType, FloatType]):
                if type(left) == type(right):
                    return left
                else:
                    return FloatType()
            else:
                raise TypeMismatchInExpression(ast)       
        if (ast.op == "="):
            res = self.typeCheck(left, right)
            if res is None and not isinstance(ast.left, AST.CallExpr):
                raise TypeMismatchInExpression(ast)
            if not type(ast.left) in [Id, ArrayCell]:
                raise NotLeftValue(ast.left)
            return res


    def visitUnaryOp(self,ast,c):
        Unary_body = self.visit(ast.body, c)
        # Check body: [body], !body, -body
        if type(Unary_body) is StringType or type(Unary_body) is ArrayType:
            raise TypeMismatchInExpression(ast)
        # Check '-', '!'
        if ast.op == '-':
            if type(Unary_body) is IntType or type(Unary_body) is FloatType:
                return FloatType() # unary negation operators -, which results in a value of type ﬂoat. 
            else: raise TypeMismatchInExpression(ast)
        else: # '!'
            if type(Unary_body) is not BoolType:
                raise TypeMismatchInExpression(ast)
            else:
                return BoolType()


    def visitArrayCell(self, ast, c):
        arrCell_arr = self.visit(ast.arr, c)
        arrCell_idx = self.visit(ast.idx, c)
        if type(arrCell_arr) in [ArrayType, ArrayPointerType] and type(arrCell_idx) is IntType:
            return arrCell_arr.eleType
        raise TypeMismatchInExpression(ast)


    def visitId(self,ast,c):
        lst = self.flatten(c[0] + c[1])
        res = self.lookup(ast.name, lst, lambda x: x.name)
        if res:
            if type(res.mtype) is not MType:
                return res.mtype
            else:
                raise Undeclared(Identifier(), ast.name)
        else:
            raise Undeclared(Identifier(), ast.name)


    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()
