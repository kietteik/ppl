# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("(\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\7\3\21\n\3\f\3\16\3\24\13\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\5\4\35\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5&\n\5")
        buf.write("\3\5\2\2\6\2\4\6\b\2\2\2(\2\n\3\2\2\2\4\22\3\2\2\2\6\34")
        buf.write("\3\2\2\2\b%\3\2\2\2\n\13\5\4\3\2\13\f\7\2\2\3\f\3\3\2")
        buf.write("\2\2\r\16\5\6\4\2\16\17\7\7\2\2\17\21\3\2\2\2\20\r\3\2")
        buf.write("\2\2\21\24\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23\25\3")
        buf.write("\2\2\2\24\22\3\2\2\2\25\26\5\6\4\2\26\5\3\2\2\2\27\30")
        buf.write("\5\b\5\2\30\31\7\b\2\2\31\32\5\b\5\2\32\35\3\2\2\2\33")
        buf.write("\35\5\b\5\2\34\27\3\2\2\2\34\33\3\2\2\2\35\7\3\2\2\2\36")
        buf.write("&\7\t\2\2\37&\7\3\2\2 &\7\4\2\2!\"\7\5\2\2\"#\5\4\3\2")
        buf.write("#$\7\6\2\2$&\3\2\2\2%\36\3\2\2\2%\37\3\2\2\2% \3\2\2\2")
        buf.write("%!\3\2\2\2&\t\3\2\2\2\5\22\34%")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INTLIT", "BOOLIT", "LB", "RB", "ADDOP", 
                      "MULOP", "ID", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_exp = 1
    RULE_term = 2
    RULE_factor = 3

    ruleNames =  [ "program", "exp", "term", "factor" ]

    EOF = Token.EOF
    INTLIT=1
    BOOLIT=2
    LB=3
    RB=4
    ADDOP=5
    MULOP=6
    ID=7
    WS=8
    ERROR_CHAR=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(MPParser.ExpContext,0)


        def EOF(self):
            return self.getToken(MPParser.EOF, 0)

        def getRuleIndex(self):
            return MPParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.exp()
            self.state = 9
            self.match(MPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.TermContext)
            else:
                return self.getTypedRuleContext(MPParser.TermContext,i)


        def ADDOP(self, i:int=None):
            if i is None:
                return self.getTokens(MPParser.ADDOP)
            else:
                return self.getToken(MPParser.ADDOP, i)

        def getRuleIndex(self):
            return MPParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = MPParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 11
                    self.term()
                    self.state = 12
                    self.match(MPParser.ADDOP) 
                self.state = 18
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 19
            self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MPParser.FactorContext)
            else:
                return self.getTypedRuleContext(MPParser.FactorContext,i)


        def MULOP(self):
            return self.getToken(MPParser.MULOP, 0)

        def getRuleIndex(self):
            return MPParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = MPParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.factor()
                self.state = 22
                self.match(MPParser.MULOP)
                self.state = 23
                self.factor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.factor()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def INTLIT(self):
            return self.getToken(MPParser.INTLIT, 0)

        def BOOLIT(self):
            return self.getToken(MPParser.BOOLIT, 0)

        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def exp(self):
            return self.getTypedRuleContext(MPParser.ExpContext,0)


        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def getRuleIndex(self):
            return MPParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = MPParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MPParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(MPParser.ID)
                pass
            elif token in [MPParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(MPParser.INTLIT)
                pass
            elif token in [MPParser.BOOLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.match(MPParser.BOOLIT)
                pass
            elif token in [MPParser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.match(MPParser.LB)
                self.state = 32
                self.exp()
                self.state = 33
                self.match(MPParser.RB)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





