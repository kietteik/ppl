# Generated from MC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MCParser import MCParser
else:
    from MCParser import MCParser

# This class defines a complete listener for a parse tree produced by MCParser.
class MCListener(ParseTreeListener):

    # Enter a parse tree produced by MCParser#exp.
    def enterExp(self, ctx:MCParser.ExpContext):
        pass

    # Exit a parse tree produced by MCParser#exp.
    def exitExp(self, ctx:MCParser.ExpContext):
        pass


    # Enter a parse tree produced by MCParser#term.
    def enterTerm(self, ctx:MCParser.TermContext):
        pass

    # Exit a parse tree produced by MCParser#term.
    def exitTerm(self, ctx:MCParser.TermContext):
        pass


    # Enter a parse tree produced by MCParser#factor.
    def enterFactor(self, ctx:MCParser.FactorContext):
        pass

    # Exit a parse tree produced by MCParser#factor.
    def exitFactor(self, ctx:MCParser.FactorContext):
        pass


    # Enter a parse tree produced by MCParser#operand.
    def enterOperand(self, ctx:MCParser.OperandContext):
        pass

    # Exit a parse tree produced by MCParser#operand.
    def exitOperand(self, ctx:MCParser.OperandContext):
        pass


