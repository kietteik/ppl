from AST import *
from Visitor import BaseVisitor
from Utils import Utils
from StaticError import *
from functools import reduce
#-------------------------------------------------------------------------#
#--------------------AUTHOR: Nguyen Minh THAM (1613166)-------------------#
#-------------------------------------------------------------------------#

class MType:

    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return 'MType([' + ','.join(str(x) for x in self.partype) + '],' + str(self.rettype) + ')'

class Symbol:

    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return 'Symbol(' + str(self.name) + ',' + str(self.mtype) + ')'

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

    def raiseRedeclared(self, kind, name, list_check, func_list):
        dupName = self.lookup(name.lower(), list_check, func_list)
        if dupName is not None:
            raise Redeclared(kind, name)
        return False

    def typeCheckBinary(self,lhs,rhs):
        if type(lhs) is IntType and type(rhs) is IntType:
            return IntType()
        elif type(lhs) in [FloatType, IntType] and type(rhs) in [FloatType, IntType]:
            return FloatType()
        return None

    def typeCheck(self,lhs,rhs,type_check = True):
        # type_check = true -> check assignment statement, mean no check arraytype,String type
        # In call function/ procedure, lhs is parameter in function/procedure and rhs is parameter pass
        if type(lhs) is type(rhs) and type(lhs) in [IntType, BoolType]:
            return lhs
        elif type(lhs) is FloatType and type(rhs) in [FloatType, IntType]:
            return FloatType()
        if (type_check== False):#check parameters in function /procdure
            if type(lhs) is StringType and type(rhs) is StringType:
                return StringType()
            if type(lhs) is ArrayType and type(rhs) is ArrayType:
                if (int(lhs.lower)==int(rhs.lower)) and (int(lhs.upper) == int(rhs.upper)) and (type(lhs.eleType) == type(rhs.eleType)):
                    return lhs
        return None 

    def callBody(self,ast,c,kind):
        at = [self.visit(x, c) for x in ast.param]
        res = self.lookup(ast.method.name.lower(), c[0], lambda x: x.name.lower())
        if res is None or not type(res.mtype) is MType:
            raise Undeclared(kind, ast.method.name)
        elif type(res.mtype.rettype) is VoidType and type(kind) is Function:
            raise Undeclared(kind, ast.method.name)
        elif type(res.mtype.rettype) is not VoidType and type(kind) is Procedure:
            raise Undeclared(kind, ast.method.name)
        elif len(ast.param) != len(res.mtype.partype):
            if type(kind) is Procedure:
                raise TypeMismatchInStatement(ast)  
            else:
                raise TypeMismatchInExpression(ast)
        else:
            for x in list(zip(res.mtype.partype,at)):
                if self.typeCheck(x[0],x[1],False) is None:
                    if type(kind) is Procedure:
                        raise TypeMismatchInStatement(ast)  
                    else:
                        raise TypeMismatchInExpression(ast)
        return res.mtype.rettype
#--------------------------------------------------------------------------------------#
#-----------------------------------FUNCTION VISIT-------------------------------------#
#--------------------------------------------------------------------------------------#

    def visitProgram(self, ast, c):
        list_gobal = c.copy()
        for _decl in ast.decl:
            if type(_decl) is VarDecl:  # Variable declaration
                self.raiseRedeclared(Variable(), _decl.variable.name, list_gobal, lambda x: x.name.lower())
                list_gobal.append(Symbol(_decl.variable.name, _decl.varType))
            elif type(_decl) is FuncDecl and type(_decl.returnType) is VoidType:  # Procedure declaration
                self.raiseRedeclared(Procedure(), _decl.name.name, list_gobal, lambda x: x.name.lower())
                list_gobal.append(Symbol(_decl.name.name, MType([i.varType for i in _decl.param], _decl.returnType)))
            else:  # Function declaration
                self.raiseRedeclared(Function(), _decl.name.name, list_gobal, lambda x: x.name.lower())
                list_gobal.append(Symbol(_decl.name.name, MType([i.varType for i in _decl.param], _decl.returnType)))
        main = self.lookup("main",list_gobal,lambda x: x.name.lower())
        if main and type(main.mtype) is MType and type(main.mtype.rettype) is VoidType and len(main.mtype.partype)==0:
            return [self.visit(x, list_gobal) for x in ast.decl]
        raise NoEntryPoint()
#----------------------------Declaration-------------------------------------#
#----------------------------------------------------------------------------#

    def visitFuncDecl(self, ast, c):
        list_local = []
        for var_decl in ast.param:
            self.raiseRedeclared(Parameter(), var_decl.variable.name, list_local, lambda x: x.name.lower())
            list_local.append(Symbol(var_decl.variable.name, var_decl.varType))
        for var_decl in ast.local:
            self.raiseRedeclared(Variable(), var_decl.variable.name, list_local, lambda x: x.name.lower())
            list_local.append(Symbol(var_decl.variable.name, var_decl.varType))
        # False -> Statements in function /procedure // True -> Statement in For / While
        at_body = list(map(lambda x: self.visit(x, (list_local+c,self.lookup(ast.name.name.lower(),c,lambda x:x.name.lower()), False)), ast.body))
        if type(ast.returnType) is not VoidType and (at_body == [] or str(at_body[::-1][0]) != "return") :
            raise FunctionNotReturn(ast.name.name)
#-------------------------------Statement--------------------------------------#
#------------------------------------------------------------------------------#

    def visitWith(self, ast, c):
        list_local = []
        for var_decl in ast.decl:
            self.raiseRedeclared(Variable(), var_decl.variable.name, list_local, lambda x: x.name.lower())
            list_local.append(Symbol(var_decl.variable.name, var_decl.varType))
        at_stmt = [self.visit(x, (list_local + c[0],c[1],c[2])) for x in ast.stmt]
        if at_stmt != []:
            return str(at_stmt[::-1][0])

    def visitAssign(self, ast, c):
        at_lhs = self.visit(ast.lhs, c)
        at_exp = self.visit(ast.exp, c)
        result = self.typeCheck(at_lhs,at_exp)
        if result is None:
            raise TypeMismatchInStatement(ast)
        return None
        
    def visitReturn(self, ast, c):
        if type(c[1].mtype.rettype) is not VoidType:#Function
            if ast.expr:
                at = self.visit(ast.expr, c)
                if self.typeCheck(c[1].mtype.rettype,at,False) is None:
                    raise TypeMismatchInStatement(ast)# function but type no same
            else:
                raise TypeMismatchInStatement(ast)# Function but return VoidType
            return "return"
        else: #procedure
            if ast.expr:
                raise TypeMismatchInStatement(ast)
            return None
     
    def visitIf(self, ast, c):
        at_expr = self.visit(ast.expr, c)
        if type(at_expr) is not BoolType:
            raise TypeMismatchInStatement(ast)
        at_thenstmt = [self.visit(x, c) for x in ast.thenStmt]
        if ast.elseStmt:
            at_elsestmt = [self.visit(x, c) for x in ast.elseStmt]
            if at_thenstmt != [] and at_elsestmt != [] and str(at_elsestmt[::-1][0]) == "return" and str(at_thenstmt[::-1][0]) == "return":
                return "return"
        return None

    def visitFor(self, ast, c):
        at_id = self.visit(ast.id, c)
        at_expr1 = self.visit(ast.expr1, c)
        at_expr2 = self.visit(ast.expr2, c)
        if type(at_id) is not IntType or type(at_expr1) is not IntType or type(at_expr2) is not IntType:
            raise TypeMismatchInStatement(ast)
        at_stmt = [self.visit(x, (c[0],c[1],True)) for x in ast.loop]
        return None
        
    def visitWhile(self, ast, c):
        at_expr = self.visit(ast.exp,c)
        if type(at_expr) is not BoolType:
            raise TypeMismatchInStatement(ast)
        at_stmt = [self.visit(x, (c[0],c[1],True)) for x in ast.sl]
        return None
    
    def visitContinue(self, ast, c):
        if not c[2]:
            raise ContinueNotInLoop() 
        return None
    
    def visitBreak(self, ast, c):
        if not c[2]:
            raise BreakNotInLoop() 
        return None

    def visitCallStmt(self, ast, c):
        return self.callBody(ast,c,Procedure())
#----------------------------------------EXPRESSION------------------------------------#
#--------------------------------------------------------------------------------------#

    def visitCallExpr(self, ast, c):
        return self.callBody(ast,c,Function())

    def visitBinaryOp(self, ast, c):
        at_left = self.visit(ast.left, c)
        at_right = self.visit(ast.right, c)
        result_type = self.typeCheckBinary(at_left,at_right)
        if ast.op in ['=', '<>', '<', '<=', '>', '>='] :
            if result_type is not None:
                return BoolType()
        elif ast.op in ['+', '-', '*', '/']:
            if result_type is not None:
                if ast.op == '/':
                    return FloatType()
                return result_type
        elif ast.op.lower() == 'div' or ast.op.lower() =='mod':
            if type(at_left) is IntType and type(at_right) is IntType:
                return IntType()
        elif ast.op.lower() == 'and' or ast.op.lower() =='or' or ast.op.lower() =='andthen' or ast.op.lower() =='orelse':
            if type(at_left) is BoolType and type(at_right) is BoolType:
                return BoolType()
        raise TypeMismatchInExpression(ast)            

    def visitUnaryOp(self, ast, c):
        at_expr = self.visit(ast.body, c)
        if ast.op == '-':
            if type(at_expr) in [IntType, FloatType]:
                return at_expr
        elif ast.op.lower() == 'not':
            if type(at_expr) is  BoolType:
                return BoolType()
        raise TypeMismatchInExpression(ast)

    def visitArrayCell(self, ast, c):
        at_arr = self.visit(ast.arr, c)
        at_idx = self.visit(ast.idx, c)
        if type(at_arr) is ArrayType and type(at_idx) is IntType:
            return at_arr.eleType
        raise TypeMismatchInExpression(ast) 

    def visitId(self, ast, c):
        res_var = self.lookup(ast.name.lower(), c[0],lambda x: x.name.lower())
        if res_var is None:
            raise Undeclared(Identifier(), ast.name)
        elif type(res_var.mtype) is  MType:
            raise Undeclared(Identifier(), ast.name)
        return res_var.mtype
#----------------------------------------EXPRESSION------------------------------------#
#--------------------------------------------------------------------------------------#

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitStringLiteral(self, ast, c):
        return StringType()