# Generated from /Users/kietteik/Documents/BKU_Stored/HK1_2020-2021/PPL/week3/initialSetup/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("\u0088\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\6\2\36\n\2\r\2\16\2\37\3\2\3\2\3\3\3\3\5\3&")
        buf.write("\n\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\5\5/\n\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\7\6:\n\6\f\6\16\6=\13\6\3\7\3")
        buf.write("\7\3\7\7\7B\n\7\f\7\16\7E\13\7\3\b\3\b\7\bI\n\b\f\b\16")
        buf.write("\bL\13\b\3\t\3\t\3\t\5\tQ\n\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\7\13^\n\13\f\13\16\13a\13\13")
        buf.write("\5\13c\n\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\5\rs\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\7\r\u0081\n\r\f\r\16\r\u0084\13\r")
        buf.write("\3\16\3\16\3\16\2\3\30\17\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\2\3\3\2\5\6\2\u008d\2\35\3\2\2\2\4%\3\2\2\2\6\'\3")
        buf.write("\2\2\2\b*\3\2\2\2\n\65\3\2\2\2\f>\3\2\2\2\16J\3\2\2\2")
        buf.write("\20P\3\2\2\2\22T\3\2\2\2\24X\3\2\2\2\26f\3\2\2\2\30r\3")
        buf.write("\2\2\2\32\u0085\3\2\2\2\34\36\5\4\3\2\35\34\3\2\2\2\36")
        buf.write("\37\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 !\3\2\2\2!\"\7\2")
        buf.write("\2\3\"\3\3\2\2\2#&\5\6\4\2$&\5\b\5\2%#\3\2\2\2%$\3\2\2")
        buf.write("\2&\5\3\2\2\2\'(\5\n\6\2()\7\n\2\2)\7\3\2\2\2*+\5\32\16")
        buf.write("\2+,\7\25\2\2,.\7\r\2\2-/\5\f\7\2.-\3\2\2\2./\3\2\2\2")
        buf.write("/\60\3\2\2\2\60\61\7\16\2\2\61\62\7\b\2\2\62\63\5\16\b")
        buf.write("\2\63\64\7\t\2\2\64\t\3\2\2\2\65\66\5\32\16\2\66;\7\25")
        buf.write("\2\2\678\7\13\2\28:\7\25\2\29\67\3\2\2\2:=\3\2\2\2;9\3")
        buf.write("\2\2\2;<\3\2\2\2<\13\3\2\2\2=;\3\2\2\2>C\5\n\6\2?@\7\n")
        buf.write("\2\2@B\5\n\6\2A?\3\2\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2")
        buf.write("D\r\3\2\2\2EC\3\2\2\2FI\5\6\4\2GI\5\20\t\2HF\3\2\2\2H")
        buf.write("G\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3\2\2\2K\17\3\2\2\2LJ")
        buf.write("\3\2\2\2MQ\5\22\n\2NQ\5\24\13\2OQ\5\26\f\2PM\3\2\2\2P")
        buf.write("N\3\2\2\2PO\3\2\2\2QR\3\2\2\2RS\7\n\2\2S\21\3\2\2\2TU")
        buf.write("\7\25\2\2UV\7\f\2\2VW\5\30\r\2W\23\3\2\2\2XY\7\25\2\2")
        buf.write("Yb\7\r\2\2Z_\5\30\r\2[\\\7\13\2\2\\^\5\30\r\2][\3\2\2")
        buf.write("\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`c\3\2\2\2a_\3\2\2\2b")
        buf.write("Z\3\2\2\2bc\3\2\2\2cd\3\2\2\2de\7\16\2\2e\25\3\2\2\2f")
        buf.write("g\7\7\2\2gh\5\30\r\2h\27\3\2\2\2ij\b\r\1\2jk\7\b\2\2k")
        buf.write("l\5\30\r\2lm\7\t\2\2ms\3\2\2\2ns\7\3\2\2os\7\4\2\2ps\7")
        buf.write("\25\2\2qs\5\24\13\2ri\3\2\2\2rn\3\2\2\2ro\3\2\2\2rp\3")
        buf.write("\2\2\2rq\3\2\2\2s\u0082\3\2\2\2tu\f\n\2\2uv\7\21\2\2v")
        buf.write("\u0081\5\30\r\13wx\f\t\2\2xy\7\22\2\2y\u0081\5\30\r\n")
        buf.write("z{\f\b\2\2{|\7\20\2\2|\u0081\5\30\r\t}~\f\7\2\2~\177\7")
        buf.write("\17\2\2\177\u0081\5\30\r\7\u0080t\3\2\2\2\u0080w\3\2\2")
        buf.write("\2\u0080z\3\2\2\2\u0080}\3\2\2\2\u0081\u0084\3\2\2\2\u0082")
        buf.write("\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083\31\3\2\2\2\u0084")
        buf.write("\u0082\3\2\2\2\u0085\u0086\t\2\2\2\u0086\33\3\2\2\2\17")
        buf.write("\37%.;CHJP_br\u0080\u0082")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'int'", "'float'", 
                     "'return'", "'{'", "'}'", "';'", "','", "'='", "'('", 
                     "')'", "'+'", "'-'", "'*'", "'/'", "':'", "'Var'" ]

    symbolicNames = [ "<INVALID>", "INTLIT", "FLOATLIT", "INT", "FLOAT", 
                      "RETURN", "LB", "RB", "SM", "CM", "EQ", "LP", "RP", 
                      "ADD", "SUB", "MUL", "DIV", "COLON", "VAR", "ID", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_dec = 1
    RULE_var_dec = 2
    RULE_func_dec = 3
    RULE_one_param = 4
    RULE_param_list = 5
    RULE_func_body = 6
    RULE_stmt = 7
    RULE_assignment = 8
    RULE_call = 9
    RULE_return_stmt = 10
    RULE_exp = 11
    RULE_type_stmt = 12

    ruleNames =  [ "program", "dec", "var_dec", "func_dec", "one_param", 
                   "param_list", "func_body", "stmt", "assignment", "call", 
                   "return_stmt", "exp", "type_stmt" ]

    EOF = Token.EOF
    INTLIT=1
    FLOATLIT=2
    INT=3
    FLOAT=4
    RETURN=5
    LB=6
    RB=7
    SM=8
    CM=9
    EQ=10
    LP=11
    RP=12
    ADD=13
    SUB=14
    MUL=15
    DIV=16
    COLON=17
    VAR=18
    ID=19
    WS=20
    ERROR_CHAR=21
    UNCLOSE_STRING=22
    ILLEGAL_ESCAPE=23
    UNTERMINATED_COMMENT=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.DecContext)
            else:
                return self.getTypedRuleContext(BKITParser.DecContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.dec()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.INT or _la==BKITParser.FLOAT):
                    break

            self.state = 31
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_dec(self):
            return self.getTypedRuleContext(BKITParser.Var_decContext,0)


        def func_dec(self):
            return self.getTypedRuleContext(BKITParser.Func_decContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_dec




    def dec(self):

        localctx = BKITParser.DecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_dec)
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.var_dec()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.func_dec()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def one_param(self):
            return self.getTypedRuleContext(BKITParser.One_paramContext,0)


        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_dec




    def var_dec(self):

        localctx = BKITParser.Var_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.one_param()
            self.state = 38
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_decContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_stmt(self):
            return self.getTypedRuleContext(BKITParser.Type_stmtContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def func_body(self):
            return self.getTypedRuleContext(BKITParser.Func_bodyContext,0)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKITParser.Param_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_dec




    def func_dec(self):

        localctx = BKITParser.Func_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_func_dec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.type_stmt()
            self.state = 41
            self.match(BKITParser.ID)
            self.state = 42
            self.match(BKITParser.LP)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.INT or _la==BKITParser.FLOAT:
                self.state = 43
                self.param_list()


            self.state = 46
            self.match(BKITParser.RP)
            self.state = 47
            self.match(BKITParser.LB)
            self.state = 48
            self.func_body()
            self.state = 49
            self.match(BKITParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class One_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_stmt(self):
            return self.getTypedRuleContext(BKITParser.Type_stmtContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ID)
            else:
                return self.getToken(BKITParser.ID, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_one_param




    def one_param(self):

        localctx = BKITParser.One_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_one_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.type_stmt()
            self.state = 52
            self.match(BKITParser.ID)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.CM:
                self.state = 53
                self.match(BKITParser.CM)
                self.state = 54
                self.match(BKITParser.ID)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def one_param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.One_paramContext)
            else:
                return self.getTypedRuleContext(BKITParser.One_paramContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.SM)
            else:
                return self.getToken(BKITParser.SM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_param_list




    def param_list(self):

        localctx = BKITParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.one_param()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.SM:
                self.state = 61
                self.match(BKITParser.SM)
                self.state = 62
                self.one_param()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_decContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_decContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_func_body




    def func_body(self):

        localctx = BKITParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INT) | (1 << BKITParser.FLOAT) | (1 << BKITParser.RETURN) | (1 << BKITParser.ID))) != 0):
                self.state = 70
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.INT, BKITParser.FLOAT]:
                    self.state = 68
                    self.var_dec()
                    pass
                elif token in [BKITParser.RETURN, BKITParser.ID]:
                    self.state = 69
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(BKITParser.SM, 0)

        def assignment(self):
            return self.getTypedRuleContext(BKITParser.AssignmentContext,0)


        def call(self):
            return self.getTypedRuleContext(BKITParser.CallContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 75
                self.assignment()
                pass

            elif la_ == 2:
                self.state = 76
                self.call()
                pass

            elif la_ == 3:
                self.state = 77
                self.return_stmt()
                pass


            self.state = 80
            self.match(BKITParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assignment




    def assignment(self):

        localctx = BKITParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(BKITParser.ID)
            self.state = 83
            self.match(BKITParser.EQ)
            self.state = 84
            self.exp(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CM)
            else:
                return self.getToken(BKITParser.CM, i)

        def getRuleIndex(self):
            return BKITParser.RULE_call




    def call(self):

        localctx = BKITParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(BKITParser.ID)
            self.state = 87
            self.match(BKITParser.LP)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INTLIT) | (1 << BKITParser.FLOATLIT) | (1 << BKITParser.LB) | (1 << BKITParser.ID))) != 0):
                self.state = 88
                self.exp(0)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.CM:
                    self.state = 89
                    self.match(BKITParser.CM)
                    self.state = 90
                    self.exp(0)
                    self.state = 95
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 98
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stmt




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(BKITParser.RETURN)
            self.state = 101
            self.exp(0)
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

        def LB(self):
            return self.getToken(BKITParser.LB, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def RB(self):
            return self.getToken(BKITParser.RB, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def call(self):
            return self.getTypedRuleContext(BKITParser.CallContext,0)


        def MUL(self):
            return self.getToken(BKITParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 104
                self.match(BKITParser.LB)
                self.state = 105
                self.exp(0)
                self.state = 106
                self.match(BKITParser.RB)
                pass

            elif la_ == 2:
                self.state = 108
                self.match(BKITParser.INTLIT)
                pass

            elif la_ == 3:
                self.state = 109
                self.match(BKITParser.FLOATLIT)
                pass

            elif la_ == 4:
                self.state = 110
                self.match(BKITParser.ID)
                pass

            elif la_ == 5:
                self.state = 111
                self.call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 126
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = BKITParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 114
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 115
                        self.match(BKITParser.MUL)
                        self.state = 116
                        self.exp(9)
                        pass

                    elif la_ == 2:
                        localctx = BKITParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 117
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 118
                        self.match(BKITParser.DIV)
                        self.state = 119
                        self.exp(8)
                        pass

                    elif la_ == 3:
                        localctx = BKITParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 120
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 121
                        self.match(BKITParser.SUB)
                        self.state = 122
                        self.exp(7)
                        pass

                    elif la_ == 4:
                        localctx = BKITParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 123
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 124
                        self.match(BKITParser.ADD)
                        self.state = 125
                        self.exp(5)
                        pass

             
                self.state = 130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Type_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKITParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_type_stmt




    def type_stmt(self):

        localctx = BKITParser.Type_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_type_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            _la = self._input.LA(1)
            if not(_la==BKITParser.INT or _la==BKITParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         




