# Given the AST declarations as follows:
class Program: #decl:List[VarDecl],stmts:List[Assign]
class VarDecl: #name:str
class Assign: #lhs:Id,rhs:Exp
class Exp(ABC): #abstract class
class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
class UnOp(Exp): #op:str,e:Exp #op is -,-., !,i2f, floor
class IntLit(Exp): #val:int
class FloatLit(Exp): #val:float
class BoolLit(Exp): #val:bool
class Id(Exp): #name:str
# and the Visitor class is declared as follows:
class StaticCheck(Visitor):
    def visitProgram(self,ctx:Program,o):pass
    def visitVarDecl(self,ctx:VarDecl,o): pass
    def visitAssign(self,ctx:Assign,o): pass
    def visitBinOp(self,ctx:BinOp,o): pass
    def visitUnOp(self,ctx:UnOp,o):pass
    def visitIntLit(self,ctx:IntLit,o): pass 
    def visitFloatLit(self,ctx,o): pass
    def visitBoolLit(self,ctx,o): pass
    def visitId(self,ctx,o): pass
# Rewrite the body of the methods in class StaticCheck to infer the type of identifiers and check the following type constraints:
# + , - , *, / accept their operands in int type and return int type
# +., -., *., /. accept their operands in float type and return float type
# > and = accept their operands in int type and return bool type
# >. and =. accept their operands in float type and return bool type
# !, &&, ||, >b and =b accept their operands in bool type and return bool type
# i2f accepts its operand in int type and return float type
# floor accept its operand in float type and return int type
# In an Assign, the type of lhs must be the same as that of rhs, otherwise, the exception TypeMismatchInStatement should be raised together with the Assign
# the type of an Id is inferred from the above constraints in the first usage, 
# if the Id is not in the declarations, exception UndeclaredIdentifier should be raised together with the name of the Id, or
# If the Id cannot be inferred in the first usage, exception TypeCannotBeInferred should be raised together with the name of the identifier
# If the expression does not conform the type constraints, the StaticCheck will raise exception TypeMismatchInExpression with the assign statement where contains the type-unresolved identifier.
# Your code starts at line 95