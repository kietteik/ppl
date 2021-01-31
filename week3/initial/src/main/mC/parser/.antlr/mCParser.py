# Generated from d:\Stu\Semester 3\Principles of Programming Languages\Tut\Tut3\test\PC_code\initial\src\main\mC\parser\mC.g4 by ANTLR 4.8
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
        buf.write("\u0093\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\6\2#\n\2\r\2\16\2$\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\7\59\n\5\f\5\16\5<\13\5\3\6\3\6\3\6\7")
        buf.write("\6A\n\6\f\6\16\6D\13\6\5\6F\n\6\3\7\3\7\7\7J\n\7\f\7\16")
        buf.write("\7M\13\7\3\b\3\b\3\b\5\bR\n\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\7\n_\n\n\f\n\16\nb\13\n\5\nd\n\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\5\fp\n\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\5\rw\n\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\7\16\u0082\n\16\f\16\16\16\u0085\13")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u008f")
        buf.write("\n\17\3\20\3\20\3\20\2\3\32\21\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36\2\3\3\2\5\6\2\u0096\2\"\3\2\2\2\4(\3\2")
        buf.write("\2\2\6+\3\2\2\2\b\64\3\2\2\2\nE\3\2\2\2\fK\3\2\2\2\16")
        buf.write("Q\3\2\2\2\20U\3\2\2\2\22Y\3\2\2\2\24g\3\2\2\2\26o\3\2")
        buf.write("\2\2\30v\3\2\2\2\32x\3\2\2\2\34\u008e\3\2\2\2\36\u0090")
        buf.write("\3\2\2\2 #\5\4\3\2!#\5\6\4\2\" \3\2\2\2\"!\3\2\2\2#$\3")
        buf.write("\2\2\2$\"\3\2\2\2$%\3\2\2\2%&\3\2\2\2&\'\7\2\2\3\'\3\3")
        buf.write("\2\2\2()\5\b\5\2)*\7\n\2\2*\5\3\2\2\2+,\5\36\20\2,-\7")
        buf.write("\25\2\2-.\7\r\2\2./\5\n\6\2/\60\7\16\2\2\60\61\7\b\2\2")
        buf.write("\61\62\5\f\7\2\62\63\7\t\2\2\63\7\3\2\2\2\64\65\5\36\20")
        buf.write("\2\65:\7\25\2\2\66\67\7\13\2\2\679\7\25\2\28\66\3\2\2")
        buf.write("\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;\t\3\2\2\2<:\3\2\2\2")
        buf.write("=B\5\b\5\2>?\7\n\2\2?A\5\b\5\2@>\3\2\2\2AD\3\2\2\2B@\3")
        buf.write("\2\2\2BC\3\2\2\2CF\3\2\2\2DB\3\2\2\2E=\3\2\2\2EF\3\2\2")
        buf.write("\2F\13\3\2\2\2GJ\5\4\3\2HJ\5\16\b\2IG\3\2\2\2IH\3\2\2")
        buf.write("\2JM\3\2\2\2KI\3\2\2\2KL\3\2\2\2L\r\3\2\2\2MK\3\2\2\2")
        buf.write("NR\5\20\t\2OR\5\22\n\2PR\5\24\13\2QN\3\2\2\2QO\3\2\2\2")
        buf.write("QP\3\2\2\2RS\3\2\2\2ST\7\n\2\2T\17\3\2\2\2UV\7\25\2\2")
        buf.write("VW\7\f\2\2WX\5\26\f\2X\21\3\2\2\2YZ\7\25\2\2Zc\7\r\2\2")
        buf.write("[`\5\26\f\2\\]\7\13\2\2]_\5\26\f\2^\\\3\2\2\2_b\3\2\2")
        buf.write("\2`^\3\2\2\2`a\3\2\2\2ad\3\2\2\2b`\3\2\2\2c[\3\2\2\2c")
        buf.write("d\3\2\2\2de\3\2\2\2ef\7\16\2\2f\23\3\2\2\2gh\7\7\2\2h")
        buf.write("i\5\26\f\2i\25\3\2\2\2jk\5\30\r\2kl\7\17\2\2lm\5\26\f")
        buf.write("\2mp\3\2\2\2np\5\30\r\2oj\3\2\2\2on\3\2\2\2p\27\3\2\2")
        buf.write("\2qr\5\32\16\2rs\7\20\2\2st\5\32\16\2tw\3\2\2\2uw\5\32")
        buf.write("\16\2vq\3\2\2\2vu\3\2\2\2w\31\3\2\2\2xy\b\16\1\2yz\5\34")
        buf.write("\17\2z\u0083\3\2\2\2{|\f\5\2\2|}\7\21\2\2}\u0082\5\34")
        buf.write("\17\2~\177\f\4\2\2\177\u0080\7\22\2\2\u0080\u0082\5\34")
        buf.write("\17\2\u0081{\3\2\2\2\u0081~\3\2\2\2\u0082\u0085\3\2\2")
        buf.write("\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\33\3")
        buf.write("\2\2\2\u0085\u0083\3\2\2\2\u0086\u008f\7\3\2\2\u0087\u008f")
        buf.write("\7\4\2\2\u0088\u008f\7\25\2\2\u0089\u008f\5\22\n\2\u008a")
        buf.write("\u008b\7\r\2\2\u008b\u008c\5\26\f\2\u008c\u008d\7\16\2")
        buf.write("\2\u008d\u008f\3\2\2\2\u008e\u0086\3\2\2\2\u008e\u0087")
        buf.write("\3\2\2\2\u008e\u0088\3\2\2\2\u008e\u0089\3\2\2\2\u008e")
        buf.write("\u008a\3\2\2\2\u008f\35\3\2\2\2\u0090\u0091\t\2\2\2\u0091")
        buf.write("\37\3\2\2\2\21\"$:BEIKQ`cov\u0081\u0083\u008e")
        return buf.getvalue()


class mCParser ( Parser ):

    grammarFileName = "mC.g4"

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
    RULE_var_dec = 1
    RULE_func_dec = 2
    RULE_params = 3
    RULE_param_list = 4
    RULE_func_body = 5
    RULE_stmt = 6
    RULE_assignment = 7
    RULE_call = 8
    RULE_return_stmt = 9
    RULE_exp = 10
    RULE_exp1 = 11
    RULE_exp2 = 12
    RULE_exp3 = 13
    RULE_type_stmt = 14

    ruleNames =  [ "program", "var_dec", "func_dec", "params", "param_list", 
                   "func_body", "stmt", "assignment", "call", "return_stmt", 
                   "exp", "exp1", "exp2", "exp3", "type_stmt" ]

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
            return self.getToken(mCParser.EOF, 0)

        def var_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mCParser.Var_decContext)
            else:
                return self.getTypedRuleContext(mCParser.Var_decContext,i)


        def func_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mCParser.Func_decContext)
            else:
                return self.getTypedRuleContext(mCParser.Func_decContext,i)


        def getRuleIndex(self):
            return mCParser.RULE_program




    def program(self):

        localctx = mCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 30
                    self.var_dec()
                    pass

                elif la_ == 2:
                    self.state = 31
                    self.func_dec()
                    pass


                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==mCParser.INT or _la==mCParser.FLOAT):
                    break

            self.state = 36
            self.match(mCParser.EOF)
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

        def params(self):
            return self.getTypedRuleContext(mCParser.ParamsContext,0)


        def SM(self):
            return self.getToken(mCParser.SM, 0)

        def getRuleIndex(self):
            return mCParser.RULE_var_dec




    def var_dec(self):

        localctx = mCParser.Var_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.params()
            self.state = 39
            self.match(mCParser.SM)
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
            return self.getTypedRuleContext(mCParser.Type_stmtContext,0)


        def ID(self):
            return self.getToken(mCParser.ID, 0)

        def LP(self):
            return self.getToken(mCParser.LP, 0)

        def param_list(self):
            return self.getTypedRuleContext(mCParser.Param_listContext,0)


        def RP(self):
            return self.getToken(mCParser.RP, 0)

        def LB(self):
            return self.getToken(mCParser.LB, 0)

        def func_body(self):
            return self.getTypedRuleContext(mCParser.Func_bodyContext,0)


        def RB(self):
            return self.getToken(mCParser.RB, 0)

        def getRuleIndex(self):
            return mCParser.RULE_func_dec




    def func_dec(self):

        localctx = mCParser.Func_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.type_stmt()
            self.state = 42
            self.match(mCParser.ID)
            self.state = 43
            self.match(mCParser.LP)
            self.state = 44
            self.param_list()
            self.state = 45
            self.match(mCParser.RP)
            self.state = 46
            self.match(mCParser.LB)
            self.state = 47
            self.func_body()
            self.state = 48
            self.match(mCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_stmt(self):
            return self.getTypedRuleContext(mCParser.Type_stmtContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(mCParser.ID)
            else:
                return self.getToken(mCParser.ID, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(mCParser.CM)
            else:
                return self.getToken(mCParser.CM, i)

        def getRuleIndex(self):
            return mCParser.RULE_params




    def params(self):

        localctx = mCParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.type_stmt()
            self.state = 51
            self.match(mCParser.ID)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mCParser.CM:
                self.state = 52
                self.match(mCParser.CM)
                self.state = 53
                self.match(mCParser.ID)
                self.state = 58
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

        def params(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mCParser.ParamsContext)
            else:
                return self.getTypedRuleContext(mCParser.ParamsContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(mCParser.SM)
            else:
                return self.getToken(mCParser.SM, i)

        def getRuleIndex(self):
            return mCParser.RULE_param_list




    def param_list(self):

        localctx = mCParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==mCParser.INT or _la==mCParser.FLOAT:
                self.state = 59
                self.params()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==mCParser.SM:
                    self.state = 60
                    self.match(mCParser.SM)
                    self.state = 61
                    self.params()
                    self.state = 66
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
                return self.getTypedRuleContexts(mCParser.Var_decContext)
            else:
                return self.getTypedRuleContext(mCParser.Var_decContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mCParser.StmtContext)
            else:
                return self.getTypedRuleContext(mCParser.StmtContext,i)


        def getRuleIndex(self):
            return mCParser.RULE_func_body




    def func_body(self):

        localctx = mCParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << mCParser.INT) | (1 << mCParser.FLOAT) | (1 << mCParser.RETURN) | (1 << mCParser.ID))) != 0):
                self.state = 71
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [mCParser.INT, mCParser.FLOAT]:
                    self.state = 69
                    self.var_dec()
                    pass
                elif token in [mCParser.RETURN, mCParser.ID]:
                    self.state = 70
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 75
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
            return self.getToken(mCParser.SM, 0)

        def assignment(self):
            return self.getTypedRuleContext(mCParser.AssignmentContext,0)


        def call(self):
            return self.getTypedRuleContext(mCParser.CallContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(mCParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return mCParser.RULE_stmt




    def stmt(self):

        localctx = mCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 76
                self.assignment()
                pass

            elif la_ == 2:
                self.state = 77
                self.call()
                pass

            elif la_ == 3:
                self.state = 78
                self.return_stmt()
                pass


            self.state = 81
            self.match(mCParser.SM)
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
            return self.getToken(mCParser.ID, 0)

        def EQ(self):
            return self.getToken(mCParser.EQ, 0)

        def exp(self):
            return self.getTypedRuleContext(mCParser.ExpContext,0)


        def getRuleIndex(self):
            return mCParser.RULE_assignment




    def assignment(self):

        localctx = mCParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(mCParser.ID)
            self.state = 84
            self.match(mCParser.EQ)
            self.state = 85
            self.exp()
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
            return self.getToken(mCParser.ID, 0)

        def LP(self):
            return self.getToken(mCParser.LP, 0)

        def RP(self):
            return self.getToken(mCParser.RP, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mCParser.ExpContext)
            else:
                return self.getTypedRuleContext(mCParser.ExpContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(mCParser.CM)
            else:
                return self.getToken(mCParser.CM, i)

        def getRuleIndex(self):
            return mCParser.RULE_call




    def call(self):

        localctx = mCParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(mCParser.ID)
            self.state = 88
            self.match(mCParser.LP)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << mCParser.INTLIT) | (1 << mCParser.FLOATLIT) | (1 << mCParser.LP) | (1 << mCParser.ID))) != 0):
                self.state = 89
                self.exp()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==mCParser.CM:
                    self.state = 90
                    self.match(mCParser.CM)
                    self.state = 91
                    self.exp()
                    self.state = 96
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 99
            self.match(mCParser.RP)
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
            return self.getToken(mCParser.RETURN, 0)

        def exp(self):
            return self.getTypedRuleContext(mCParser.ExpContext,0)


        def getRuleIndex(self):
            return mCParser.RULE_return_stmt




    def return_stmt(self):

        localctx = mCParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(mCParser.RETURN)
            self.state = 102
            self.exp()
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

        def exp1(self):
            return self.getTypedRuleContext(mCParser.Exp1Context,0)


        def ADD(self):
            return self.getToken(mCParser.ADD, 0)

        def exp(self):
            return self.getTypedRuleContext(mCParser.ExpContext,0)


        def getRuleIndex(self):
            return mCParser.RULE_exp




    def exp(self):

        localctx = mCParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exp)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.exp1()
                self.state = 105
                self.match(mCParser.ADD)
                self.state = 106
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mCParser.Exp2Context)
            else:
                return self.getTypedRuleContext(mCParser.Exp2Context,i)


        def SUB(self):
            return self.getToken(mCParser.SUB, 0)

        def getRuleIndex(self):
            return mCParser.RULE_exp1




    def exp1(self):

        localctx = mCParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_exp1)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.exp2(0)
                self.state = 112
                self.match(mCParser.SUB)
                self.state = 113
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(mCParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(mCParser.Exp2Context,0)


        def MUL(self):
            return self.getToken(mCParser.MUL, 0)

        def DIV(self):
            return self.getToken(mCParser.DIV, 0)

        def getRuleIndex(self):
            return mCParser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mCParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.exp3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 127
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = mCParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 121
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 122
                        self.match(mCParser.MUL)
                        self.state = 123
                        self.exp3()
                        pass

                    elif la_ == 2:
                        localctx = mCParser.Exp2Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                        self.state = 124
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 125
                        self.match(mCParser.DIV)
                        self.state = 126
                        self.exp3()
                        pass

             
                self.state = 131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(mCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(mCParser.FLOATLIT, 0)

        def ID(self):
            return self.getToken(mCParser.ID, 0)

        def call(self):
            return self.getTypedRuleContext(mCParser.CallContext,0)


        def LP(self):
            return self.getToken(mCParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(mCParser.ExpContext,0)


        def RP(self):
            return self.getToken(mCParser.RP, 0)

        def getRuleIndex(self):
            return mCParser.RULE_exp3




    def exp3(self):

        localctx = mCParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exp3)
        try:
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(mCParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(mCParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.match(mCParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.call()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 136
                self.match(mCParser.LP)
                self.state = 137
                self.exp()
                self.state = 138
                self.match(mCParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(mCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(mCParser.FLOAT, 0)

        def getRuleIndex(self):
            return mCParser.RULE_type_stmt




    def type_stmt(self):

        localctx = mCParser.Type_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_type_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not(_la==mCParser.INT or _la==mCParser.FLOAT):
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
        self._predicates[12] = self.exp2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




