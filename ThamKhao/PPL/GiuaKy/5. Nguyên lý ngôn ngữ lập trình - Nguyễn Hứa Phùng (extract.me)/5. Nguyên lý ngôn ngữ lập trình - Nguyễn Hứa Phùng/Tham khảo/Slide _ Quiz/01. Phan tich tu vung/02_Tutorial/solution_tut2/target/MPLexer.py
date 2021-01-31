# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("X\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\7\3\7\3\7\6\79\n\7\r\7\16\7:\3\b\6\b>\n\b\r\b\16\b")
        buf.write("?\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\6\16")
        buf.write("M\n\16\r\16\16\16N\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\2\2\22\3\3\5\4\7\5\t\2\13\2\r\6\17\7\21\b\23\t\25")
        buf.write("\n\27\13\31\f\33\r\35\16\37\17!\20\3\2\5\3\2c|\3\2\62")
        buf.write(";\5\2\13\f\17\17\"\"\2Y\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5(")
        buf.write("\3\2\2\2\7,\3\2\2\2\t\61\3\2\2\2\13\63\3\2\2\2\r\65\3")
        buf.write("\2\2\2\17=\3\2\2\2\21A\3\2\2\2\23C\3\2\2\2\25E\3\2\2\2")
        buf.write("\27G\3\2\2\2\31I\3\2\2\2\33L\3\2\2\2\35R\3\2\2\2\37T\3")
        buf.write("\2\2\2!V\3\2\2\2#$\7o\2\2$%\7c\2\2%&\7k\2\2&\'\7p\2\2")
        buf.write("\'\4\3\2\2\2()\7k\2\2)*\7p\2\2*+\7v\2\2+\6\3\2\2\2,-\7")
        buf.write("x\2\2-.\7q\2\2./\7k\2\2/\60\7f\2\2\60\b\3\2\2\2\61\62")
        buf.write("\t\2\2\2\62\n\3\2\2\2\63\64\t\3\2\2\64\f\3\2\2\2\658\5")
        buf.write("\t\5\2\669\5\13\6\2\679\5\t\5\28\66\3\2\2\28\67\3\2\2")
        buf.write("\29:\3\2\2\2:8\3\2\2\2:;\3\2\2\2;\16\3\2\2\2<>\t\3\2\2")
        buf.write("=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2@\20\3\2\2\2A")
        buf.write("B\7*\2\2B\22\3\2\2\2CD\7+\2\2D\24\3\2\2\2EF\7}\2\2F\26")
        buf.write("\3\2\2\2GH\7\177\2\2H\30\3\2\2\2IJ\7=\2\2J\32\3\2\2\2")
        buf.write("KM\t\4\2\2LK\3\2\2\2MN\3\2\2\2NL\3\2\2\2NO\3\2\2\2OP\3")
        buf.write("\2\2\2PQ\b\16\2\2Q\34\3\2\2\2RS\13\2\2\2S\36\3\2\2\2T")
        buf.write("U\13\2\2\2U \3\2\2\2VW\13\2\2\2W\"\3\2\2\2\7\28:?N\3\b")
        buf.write("\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    ID = 4
    INTLIT = 5
    LB = 6
    RB = 7
    LP = 8
    RP = 9
    SEMI = 10
    WS = 11
    ERROR_CHAR = 12
    UNCLOSE_STRING = 13
    ILLEGAL_ESCAPE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", "LP", "RP", 
            "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "LETTER", "NUMBER", "ID", 
                  "INTLIT", "LB", "RB", "LP", "RP", "SEMI", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


