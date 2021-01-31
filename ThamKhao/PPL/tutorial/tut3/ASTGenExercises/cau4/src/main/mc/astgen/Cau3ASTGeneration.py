from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
import functools

class ASTGeneration(MCVisitor):
	# exp: term COMPARE term | term ;
    def visitExp(self,ctx:MCParser.ExpContext):
        if ctx.getChildCount() == 3:
            term1 = ctx.term(0).accept(self)
            term2 = ctx.term(1).accept(self)
            compare = ctx.COMPARE().getText()

            return Binary(compare, term1, term2) # return a Binary object for the first right hand side
        else:
            term1 = ctx.term(0).accept(self)
            return term1 # generate code for the second right hand side

    # term: factor EXPONENT term | factor ;
    def visitTerm(self,ctx:MCParser.TermContext):
        factor = ctx.factor().accept(self)

        if ctx.getChildCount() == 3:
            exponent = ctx.EXPONENT().getText()
            term = ctx.term().accept(self)

            return Binary(exponent, factor, term)# return a Binary object for the first right hand side
        else:
            return factor # generate code for the second right hand side

    # factor: operand (ANDOR operand)* ; 
    def visitFactor(self,ctx:MCParser.FactorContext):
        if(ctx.getChildCount() != 1):
            from functools import reduce
            operand = ctx.operand()
            andor = ctx.ANDOR()
            genList = list(zip(operand[1:], andor))

            return reduce(lambda acc, i: Binary(i[1].getText(), acc, self.visit(i[0])), genList, self.visit(ctx.operand(0)))

        return self.visit(ctx.operand(0)) # return a Binary object 
  
  	# operand: INTLIT | BOOLIT | LB exp RB ;
    def visitOperand(self,ctx:MCParser.OperandContext):
        if ctx.getChildCount() == 3:
            return ctx.exp().accept(self) # generate code for the third right hand side
        elif ctx.INTLIT():
            intlit = ctx.INTLIT().getText()
            return IntLit(int(intlit)) # return a IntLit object
        else:
            boollit = ctx.BOOLIT().getText()  
            return BoolLit(boollit == "true")

