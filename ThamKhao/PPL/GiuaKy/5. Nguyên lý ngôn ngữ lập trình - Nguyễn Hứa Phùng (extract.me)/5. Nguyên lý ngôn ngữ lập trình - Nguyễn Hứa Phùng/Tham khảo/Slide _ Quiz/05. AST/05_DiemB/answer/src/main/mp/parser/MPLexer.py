# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write(";\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\6\2\27\n\2\r\2\16\2\30\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3$\n\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\6\b/\n\b\r\b\16\b\60\3\t\6")
        buf.write("\t\64\n\t\r\t\16\t\65\3\t\3\t\3\n\3\n\2\2\13\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\3\2\7\3\2\62;\4\2--//")
        buf.write("\4\2,,\61\61\3\2c|\5\2\13\f\17\17\"\"\2>\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\3\26\3\2")
        buf.write("\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13)\3\2\2\2\r+")
        buf.write("\3\2\2\2\17.\3\2\2\2\21\63\3\2\2\2\239\3\2\2\2\25\27\t")
        buf.write("\2\2\2\26\25\3\2\2\2\27\30\3\2\2\2\30\26\3\2\2\2\30\31")
        buf.write("\3\2\2\2\31\4\3\2\2\2\32\33\7V\2\2\33\34\7t\2\2\34\35")
        buf.write("\7w\2\2\35$\7g\2\2\36\37\7H\2\2\37 \7c\2\2 !\7n\2\2!\"")
        buf.write("\7u\2\2\"$\7g\2\2#\32\3\2\2\2#\36\3\2\2\2$\6\3\2\2\2%")
        buf.write("&\7*\2\2&\b\3\2\2\2\'(\7+\2\2(\n\3\2\2\2)*\t\3\2\2*\f")
        buf.write("\3\2\2\2+,\t\4\2\2,\16\3\2\2\2-/\t\5\2\2.-\3\2\2\2/\60")
        buf.write("\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\20\3\2\2\2\62\64")
        buf.write("\t\6\2\2\63\62\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2\2\65")
        buf.write("\66\3\2\2\2\66\67\3\2\2\2\678\b\t\2\28\22\3\2\2\29:\13")
        buf.write("\2\2\2:\24\3\2\2\2\7\2\30#\60\65\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    BOOLIT = 2
    LB = 3
    RB = 4
    ADDOP = 5
    MULOP = 6
    ID = 7
    WS = 8
    ERROR_CHAR = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "BOOLIT", "LB", "RB", "ADDOP", "MULOP", "ID", "WS", 
            "ERROR_CHAR" ]

    ruleNames = [ "INTLIT", "BOOLIT", "LB", "RB", "ADDOP", "MULOP", "ID", 
                  "WS", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


