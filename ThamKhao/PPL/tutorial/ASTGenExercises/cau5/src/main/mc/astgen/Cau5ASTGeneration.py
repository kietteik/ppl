from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *

class ASTGeneration(MCVisitor):
    # program: vardecl+ EOF;
    def visitProgram(self,ctx:MCParser.ProgramContext):
        from functools import reduce
        reVal = reduce(lambda acc, i: acc + self.visit(i), ctx.vardecl(), [])
        return Program(reVal) # return a Program object

    # vardecl: mctype manyvar ;
    def visitVardecl(self,ctx:MCParser.VardeclContext):
        mctype = self.visit(ctx.mctype())
        manyvar = self.visit(ctx.manyvar())

        return [VarDecl(ArrayType(mctype, i[1]), i[0]) if i[1] is not None else VarDecl(mctype, i[0]) for i in manyvar ] # return the list of VarDecl
  	
    # mctype: INTTYPE | FLOATTYPE ;
    def visitMctype(self,ctx:MCParser.MctypeContext):
        if ctx.INTTYPE():
            return IntType()
        else:
            return FloatType()

    # manyvar: var (COMMA var)* ;
    def visitManyvar(self,ctx:MCParser.ManyvarContext):
        return [ self.visit(i) for i in ctx.var() ]

    # var: ID (LSB INTLIT RSB)? ;
    def visitVar(self,ctx:MCParser.VarContext):
        return (ctx.ID().getText(), int(ctx.INTLIT().getText()) if ctx.INTLIT() else None)