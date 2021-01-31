from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *
from functools import reduce

class ASTGeneration(MPVisitor):
    def toBool(self,x):
        return x == "True"

    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.ADDOP():
            lstTerm = ctx.term()
            lstADDOP = ctx.ADDOP()
            mergeLst=list(zip(lstADDOP,lstTerm[1:]))
            return reduce(lambda x,y: Add(x,self.visit(y[1])) if y[0].getText() == '+' else Minus(x,self.visit(y[1])),mergeLst,self.visit(ctx.term(0)) )
        else:
            return self.visit(ctx.term(0))
    
    def visitTerm(self,ctx:MPParser.TermContext):
        if ctx.term():
            if ctx.MULOP().getText() == '*':
                return Mul(self.visit(ctx.term()),self.visit(ctx.factor()))
            else:
                return Div(self.visit(ctx.term()),self.visit(ctx.factor()))
        else:
            return self.visit(ctx.factor())


    def visitFactor(self,ctx:MPParser.FactorContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLIT():
            return BooleanLiteral(self.toBool(ctx.BOOLIT().getText()))
        else:
            return self.visit(ctx.exp())