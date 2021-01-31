from MCVisitor import MCVisitor
from MCParser import MCParser
from AST import *
import functools

class ASTGeneration(MCVisitor):
	# exp: term COMPARE term | term ;
    def visitExp(self,ctx:MCParser.ExpContext):
        if ctx.getChildCount() == 3:
            return Binary(ctx.COMPARE().getText(), self.visit(ctx.term(0)), self.visit(ctx.term(1))) # return a Binary object for the first right hand side
        else:
            return self.visit(ctx.term(0)) # generate code for the second right hand side

    # term: factor EXPONENT term | factor ;
    def visitTerm(self,ctx:MCParser.TermContext):
        if ctx.getChildCount() == 3:
            return Binary(ctx.EXPONENT().getText(), self.visit(ctx.factor()), self.visit(ctx.term())) # return a Binary object for the first right hand side
        else:
            return self.visit(ctx.factor()) # generate code for the second right hand side

    # factor: operand (ANDOR operand)* ; 
    def visitFactor(self,ctx:MCParser.FactorContext):
        from functools import reduce

        if(ctx.getChildCount() != 1):
            operand = ctx.operand()
            andor = ctx.ANDOR()

            lst = list(zip(andor, operand[1:]))

            return reduce(lambda acc, i: Binary(i[0].getText(), acc, self.visit(i[1])), lst, self.visit(ctx.operand(0)))

        return self.visit(ctx.operand(0)) # return a Binary object 
  
  	# operand: INTLIT | BOOLIT | LB exp RB ;
    def visitOperand(self,ctx:MCParser.OperandContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.exp()) # generate code for the third right hand side
        elif ctx.INTLIT():
            return IntLit(int(ctx.INTLIT().getText())) # return a IntLit object
        return BoolLit(ctx.BOOLIT().getText() == 'true') # return a BoolLit object

