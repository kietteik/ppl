from dataclasses import dataclass
from typing import List, Tuple

def printlist(lst,f=str,start="[",sepa=",",ending="]"):
	return start + sepa.join(f(i) for i in lst) + ending

class Exp: #abstract class
	def accept(self, visitor, param):
		pass

@dataclass
class BinOp(Exp): 
	op:str
	e1:Exp
	e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
	def __str__(self):
		return "BinOp(" + self.op + ',' + str(self.e1) + ',' + str(self.e2) + ')' 
	def accept(self, visitor, param):
		return visitor.visitBinOp(self, param)

@dataclass
class UnOp(Exp): 
	op:str
	e:Exp #op is -,-., !,i2f, floor
	def __str__(self):
		return "UnOp(" + self.op + ',' + str(self.e) + ')' 
	def accept(self, visitor, param):
		return visitor.visitUnOp(self, param)

@dataclass
class IntLit(Exp): 
	val:int
	def __str__(self):
		return "IntLit(" + str(self.val) + ')' 
	def accept(self, visitor, param):
		return visitor.visitIntLit(self, param)

@dataclass
class FloatLit(Exp): 
	val:float
	def __str__(self):
		return "FloatLit(" + str(self.val) + ')' 
	def accept(self, visitor, param):
		return visitor.visitFloatLit(self, param)

@dataclass
class BoolLit(Exp): 
	val:bool
	def __str__(self):
		return "BoolLit(" + str(self.val) + ')' 
	def accept(self, visitor, param):
		return visitor.visitBoolLit(self, param)

@dataclass
class Id(Exp): 
	name:str
	def __str__(self):
		return "Id(" + self.name + ')' 
	def accept(self, visitor, param):
		return visitor.visitId(self, param)

@dataclass
class VarDecl: 
	name:str
	def __str__(self):
		return "VarDecl(" + self.name + ')' 
	def accept(self, visitor, param):
		return visitor.visitVarDecl(self, param)

@dataclass
class Assign: 
	lhs:Id
	rhs:Exp
	def __str__(self):
		return "Assign(" + str(self.lhs) + ',' + str(self.rhs) + ')' 
	def accept(self, visitor, param):
		return visitor.visitAssign(self, param)

@dataclass
class Program: 
	decl:List[VarDecl]
	stmts:List[Assign]
	def __str__(self):
		return "Program(" + printlist(self.decl) + ',' + printlist(self.stmts) + ')' 
	def accept(self, visitor, param):
		return visitor.visitProgram(self, param)

@dataclass
class TypeMismatchInExpression (Exception): 
	name:Exp
	def __str__(self):
		return "Type Mismatch In Expression: " + str(self.name)

@dataclass
class TypeMismatchInStatement(Exception): 
	name:Assign
	def __str__(self):
		return "Type Mismatch In Statement: " + str(self.name)

@dataclass
class TypeCannotBeInferred(Exception): 
	name:Assign
	def __str__(self):
		return "Type Cannot Be Inferred: " + str(self.name)

@dataclass
class UndeclaredIdentifier(Exception): 
	name:Id
	def __str__(self):
		return "Undeclared Identifier: " + self.name


from functools import reduce
class Visitor:
    def visitProgram(self,ctx:Program,o):
        o = {}
        env = [x.accept(self, o) for x in ctx.decl]
        env2 = [x.accept(self, o) for x in ctx.stmts]

    def visitVarDecl(self,ctx:VarDecl,o): 
        o[ctx.name] = ctx.name

    def visitAssign(self,ctx:Assign,o):
        rtype = ctx.rhs.accept(self, o)
        ltype = ctx.lhs.accept(self, o)
        if ltype not in ['int', 'float', 'bool']:
            if rtype not in ['int', 'float', 'bool']:
                raise TypeCannotBeInferred(ctx)
            o[ltype] = rtype
            # ltype = rtype
        elif ltype != rtype:
            raise TypeMismatchInStatement(ctx)

    def visitBinOp(self,ctx:BinOp,o):
        ltype = ctx.e1.accept(self, o)
        rtype = ctx.e2.accept(self, o)
        if ctx.op in ['+', '-', '*', '/']:
            if ltype in ['bool', 'float'] or rtype in ['bool', 'float']:
                raise TypeMismatchInExpression(ctx)
            if ltype != 'int':
                o[ltype] = 'int'
            if rtype != 'int':
                o[rtype] = 'int'
            return 'int'
            
        elif ctx.op in ['+.', '-.', '*.', '/.']:
            if ltype in ['bool', 'int'] or rtype in ['bool', 'int']:
                raise TypeMismatchInExpression(ctx)
            if ltype != 'float':
                o[ltype] = 'float'
            if rtype != 'float':
                o[rtype] = 'float'
            return 'float'
        elif ctx.op in ['>', '=']:
            if ltype in ['bool', 'float'] or rtype in ['bool', 'float']:
                raise TypeMismatchInExpression(ctx)
            if ltype != 'int':
                o[ltype] = 'int'
            if rtype != 'int':
                o[rtype] = 'int'
            return 'bool'
        elif ctx.op in ['>.','=.']:
            if ltype in ['bool', 'int'] or rtype in ['bool', 'int']:
                raise TypeMismatchInExpression(ctx)
            if ltype != 'float':
                o[ltype] = 'float'
            if rtype != 'float':
                o[rtype] = 'float'
            return 'bool'
        elif ctx.op in ['&&','||','>b','=b']:
            if ltype in ['int', 'float'] or rtype in ['int', 'float']:
                raise TypeMismatchInExpression(ctx)
            if ltype != 'bool':
                o[ltype] = 'bool'
            if rtype != 'bool':
                o[rtype] = 'bool'
            return 'bool'
            
    def visitUnOp(self,ctx:UnOp,o):
        exp = ctx.e.accept(self, o)
        if ctx.op == '-':
            if exp in ['float', 'bool']:
       	        raise TypeMismatchInExpression(ctx)
            if exp != 'int':
                o[exp] = 'int'
            return 'int'
       	elif ctx.op == '-.':
       	    if exp in ['int', 'bool']:
       	        raise TypeMismatchInExpression(ctx)
            if exp != 'float':
                o[exp] = 'float'
            return 'float'
        elif ctx.op == '!':
            if exp in ['float', 'int']:
       	        raise TypeMismatchInExpression(ctx)
            if exp != 'bool':
                o[exp] = 'bool'
            return 'bool'
       	elif ctx.op == 'i2f':
       	    if exp in ['float', 'bool']:
       	        raise TypeMismatchInExpression(ctx)
            if exp != 'int':
                o[exp] = 'int'
            return 'float'  
       	elif ctx.op == 'floor':
       	    if exp in ['int', 'bool']:
       	        raise TypeMismatchInExpression(ctx)
            if exp != 'float':
                o[exp] = 'float'
            return 'int' 

    def visitIntLit(self,ctx:IntLit,o):
        return 'int'

    def visitFloatLit(self,ctx,o):
        return 'float'

    def visitBoolLit(self,ctx,o): 
        return 'bool'

    def visitId(self,ctx,o):
        if ctx.name in o:
            return o[ctx.name]
        raise UndeclaredIdentifier(ctx.name)    

# x = Program([VarDecl("x")],[Assign(Id("x"),BinOp("+",IntLit(3),BoolLit(True)))])
# x = Program([VarDecl("x")],[Assign(Id("x"),BinOp("*",BinOp("+",Id("x"),IntLit(3.4)),BinOp("-",Id("x"),FloatLit(2.1))))])
# x = Program([VarDecl("x"),VarDecl("y")],[Assign(Id("x"),Id("y"))])
x = Program([VarDecl("x"),VarDecl("y"),VarDecl("z")],[Assign(Id("x"),BinOp(">b",BinOp("&&",Id("x"),Id("y")),BinOp("||",BoolLit(False),BinOp(">",Id("z"),IntLit(3))))),Assign(Id("z"),Id("x"))])
# x = Program([VarDecl("x"),VarDecl("y"),VarDecl("z")],[Assign(Id("x"),UnOp("!",BinOp("=",Id("z"),BinOp("*",Id("y"),Id("x")))))])

x.accept(Visitor(), [])