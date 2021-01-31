# Generated from /Users/kietteik/Documents/BKU_Stored/HK1_2020-2021/PPL/Asm2/initial/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete listener for a parse tree produced by BKITParser.
class BKITListener(ParseTreeListener):

    # Enter a parse tree produced by BKITParser#program.
    def enterProgram(self, ctx:BKITParser.ProgramContext):
        pass

    # Exit a parse tree produced by BKITParser#program.
    def exitProgram(self, ctx:BKITParser.ProgramContext):
        pass


    # Enter a parse tree produced by BKITParser#exp.
    def enterExp(self, ctx:BKITParser.ExpContext):
        pass

    # Exit a parse tree produced by BKITParser#exp.
    def exitExp(self, ctx:BKITParser.ExpContext):
        pass


    # Enter a parse tree produced by BKITParser#term.
    def enterTerm(self, ctx:BKITParser.TermContext):
        pass

    # Exit a parse tree produced by BKITParser#term.
    def exitTerm(self, ctx:BKITParser.TermContext):
        pass


    # Enter a parse tree produced by BKITParser#factor.
    def enterFactor(self, ctx:BKITParser.FactorContext):
        pass

    # Exit a parse tree produced by BKITParser#factor.
    def exitFactor(self, ctx:BKITParser.FactorContext):
        pass


    # Enter a parse tree produced by BKITParser#operand.
    def enterOperand(self, ctx:BKITParser.OperandContext):
        pass

    # Exit a parse tree produced by BKITParser#operand.
    def exitOperand(self, ctx:BKITParser.OperandContext):
        pass



del BKITParser