# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3+")
        buf.write("\17\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\2\2\4\2\4\2\2\2\f\2\6\3\2\2\2\4\f\3\2\2\2\6\7\7\23")
        buf.write("\2\2\7\b\7\33\2\2\b\t\7\'\2\2\t\n\7\36\2\2\n\13\7\2\2")
        buf.write("\3\13\3\3\2\2\2\f\r\7%\2\2\r\5\3\2\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Body'", "'Break'", "'Continue'", "'Do'", 
                     "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", 
                     "'EndWhile'", "'For'", "'Function'", "'If'", "'Parameter'", 
                     "'Return'", "'Then'", "'Var'", "'While'", "'True'", 
                     "'False'", "'['", "']'", "'('", "')'", "':'", "'.'", 
                     "','", "';'" ]

    symbolicNames = [ "<INVALID>", "KEY_BODY", "KEY_BREAK", "KEY_CONTINUE", 
                      "KEY_DO", "KEY_ELSE", "KEY_ELSEIF", "KEY_ENDBODY", 
                      "KEY_ENDIF", "KEY_ENDFOR", "KEY_ENDWHILE", "KEY_FOR", 
                      "KEY_FUNCTION", "KEY_IF", "KEY_PARAMETER", "KEY_RETURN", 
                      "KEY_THEN", "KEY_VAR", "KEY_WHILE", "KEY_TRUE", "KEY_FALSE", 
                      "LSB", "RSB", "LP", "RP", "CL", "DOT", "CM", "SM", 
                      "DECIMAL", "HEX", "OCTAL", "INTLIT", "FLOATLIT", "BOOL", 
                      "ESCAPE_SEQUENCE", "STRINGLIT", "ID", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_string = 1

    ruleNames =  [ "program", "string" ]

    EOF = Token.EOF
    KEY_BODY=1
    KEY_BREAK=2
    KEY_CONTINUE=3
    KEY_DO=4
    KEY_ELSE=5
    KEY_ELSEIF=6
    KEY_ENDBODY=7
    KEY_ENDIF=8
    KEY_ENDFOR=9
    KEY_ENDWHILE=10
    KEY_FOR=11
    KEY_FUNCTION=12
    KEY_IF=13
    KEY_PARAMETER=14
    KEY_RETURN=15
    KEY_THEN=16
    KEY_VAR=17
    KEY_WHILE=18
    KEY_TRUE=19
    KEY_FALSE=20
    LSB=21
    RSB=22
    LP=23
    RP=24
    CL=25
    DOT=26
    CM=27
    SM=28
    DECIMAL=29
    HEX=30
    OCTAL=31
    INTLIT=32
    FLOATLIT=33
    BOOL=34
    ESCAPE_SEQUENCE=35
    STRINGLIT=36
    ID=37
    WS=38
    ERROR_CHAR=39
    UNCLOSE_STRING=40
    ILLEGAL_ESCAPE=41

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEY_VAR(self):
            return self.getToken(BKITParser.KEY_VAR, 0)

        def CL(self):
            return self.getToken(BKITParser.CL, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(BKITParser.KEY_VAR)
            self.state = 5
            self.match(BKITParser.CL)
            self.state = 6
            self.match(BKITParser.ID)
            self.state = 7
            self.match(BKITParser.SM)
            self.state = 8
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCAPE_SEQUENCE(self):
            return self.getToken(BKITParser.ESCAPE_SEQUENCE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = BKITParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(BKITParser.ESCAPE_SEQUENCE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





