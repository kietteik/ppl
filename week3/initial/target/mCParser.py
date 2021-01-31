# Generated from main/mC/parser/mC.g4 by ANTLR 4.8
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
        buf.write("\u0083\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\6\2\35\n\2\r\2\16\2\36\3\2\3\2\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\5\4*\n\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\7\5\65\n\5\f\5\16\58\13\5\3\6\3\6\3\6\7\6=\n\6\f\6")
        buf.write("\16\6@\13\6\3\7\3\7\7\7D\n\7\f\7\16\7G\13\7\3\b\3\b\3")
        buf.write("\b\5\bL\n\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\7\nY\n\n\f\n\16\n\\\13\n\5\n^\n\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\fn\n\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\f|\n\f")
        buf.write("\f\f\16\f\177\13\f\3\r\3\r\3\r\2\3\26\16\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\2\3\3\2\5\6\2\u0089\2\34\3\2\2\2\4\"\3")
        buf.write("\2\2\2\6%\3\2\2\2\b\60\3\2\2\2\n9\3\2\2\2\fE\3\2\2\2\16")
        buf.write("K\3\2\2\2\20O\3\2\2\2\22S\3\2\2\2\24a\3\2\2\2\26m\3\2")
        buf.write("\2\2\30\u0080\3\2\2\2\32\35\5\4\3\2\33\35\5\6\4\2\34\32")
        buf.write("\3\2\2\2\34\33\3\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36")
        buf.write("\37\3\2\2\2\37 \3\2\2\2 !\7\2\2\3!\3\3\2\2\2\"#\5\b\5")
        buf.write("\2#$\7\n\2\2$\5\3\2\2\2%&\5\30\r\2&\'\7\25\2\2\')\7\r")
        buf.write("\2\2(*\5\n\6\2)(\3\2\2\2)*\3\2\2\2*+\3\2\2\2+,\7\16\2")
        buf.write("\2,-\7\b\2\2-.\5\f\7\2./\7\t\2\2/\7\3\2\2\2\60\61\5\30")
        buf.write("\r\2\61\66\7\25\2\2\62\63\7\13\2\2\63\65\7\25\2\2\64\62")
        buf.write("\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67\t")
        buf.write("\3\2\2\28\66\3\2\2\29>\5\b\5\2:;\7\n\2\2;=\5\b\5\2<:\3")
        buf.write("\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?\13\3\2\2\2@>\3\2")
        buf.write("\2\2AD\5\4\3\2BD\5\16\b\2CA\3\2\2\2CB\3\2\2\2DG\3\2\2")
        buf.write("\2EC\3\2\2\2EF\3\2\2\2F\r\3\2\2\2GE\3\2\2\2HL\5\20\t\2")
        buf.write("IL\5\22\n\2JL\5\24\13\2KH\3\2\2\2KI\3\2\2\2KJ\3\2\2\2")
        buf.write("LM\3\2\2\2MN\7\n\2\2N\17\3\2\2\2OP\7\25\2\2PQ\7\f\2\2")
        buf.write("QR\5\26\f\2R\21\3\2\2\2ST\7\25\2\2T]\7\r\2\2UZ\5\26\f")
        buf.write("\2VW\7\13\2\2WY\5\26\f\2XV\3\2\2\2Y\\\3\2\2\2ZX\3\2\2")
        buf.write("\2Z[\3\2\2\2[^\3\2\2\2\\Z\3\2\2\2]U\3\2\2\2]^\3\2\2\2")
        buf.write("^_\3\2\2\2_`\7\16\2\2`\23\3\2\2\2ab\7\7\2\2bc\5\26\f\2")
        buf.write("c\25\3\2\2\2de\b\f\1\2ef\7\b\2\2fg\5\26\f\2gh\7\t\2\2")
        buf.write("hn\3\2\2\2in\7\3\2\2jn\7\4\2\2kn\7\25\2\2ln\5\22\n\2m")
        buf.write("d\3\2\2\2mi\3\2\2\2mj\3\2\2\2mk\3\2\2\2ml\3\2\2\2n}\3")
        buf.write("\2\2\2op\f\n\2\2pq\7\21\2\2q|\5\26\f\13rs\f\t\2\2st\7")
        buf.write("\22\2\2t|\5\26\f\nuv\f\b\2\2vw\7\20\2\2w|\5\26\f\txy\f")
        buf.write("\7\2\2yz\7\17\2\2z|\5\26\f\7{o\3\2\2\2{r\3\2\2\2{u\3\2")
        buf.write("\2\2{x\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\27\3")
        buf.write("\2\2\2\177}\3\2\2\2\u0080\u0081\t\2\2\2\u0081\31\3\2\2")
        buf.write("\2\17\34\36)\66>CEKZ]m{}")
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
    RULE_one_param = 3
    RULE_param_list = 4
    RULE_func_body = 5
    RULE_stmt = 6
    RULE_assignment = 7
    RULE_call = 8
    RULE_return_stmt = 9
    RULE_exp = 10
    RULE_type_stmt = 11

    ruleNames =  [ "program", "var_dec", "func_dec", "one_param", "param_list", 
                   "func_body", "stmt", "assignment", "call", "return_stmt", 
                   "exp", "type_stmt" ]

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = mCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 24
                    self.var_dec()
                    pass

                elif la_ == 2:
                    self.state = 25
                    self.func_dec()
                    pass


                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==mCParser.INT or _la==mCParser.FLOAT):
                    break

            self.state = 30
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

        def one_param(self):
            return self.getTypedRuleContext(mCParser.One_paramContext,0)


        def SM(self):
            return self.getToken(mCParser.SM, 0)

        def getRuleIndex(self):
            return mCParser.RULE_var_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dec" ):
                return visitor.visitVar_dec(self)
            else:
                return visitor.visitChildren(self)




    def var_dec(self):

        localctx = mCParser.Var_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_var_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.one_param()
            self.state = 33
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

        def RP(self):
            return self.getToken(mCParser.RP, 0)

        def LB(self):
            return self.getToken(mCParser.LB, 0)

        def func_body(self):
            return self.getTypedRuleContext(mCParser.Func_bodyContext,0)


        def RB(self):
            return self.getToken(mCParser.RB, 0)

        def param_list(self):
            return self.getTypedRuleContext(mCParser.Param_listContext,0)


        def getRuleIndex(self):
            return mCParser.RULE_func_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_dec" ):
                return visitor.visitFunc_dec(self)
            else:
                return visitor.visitChildren(self)




    def func_dec(self):

        localctx = mCParser.Func_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func_dec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.type_stmt()
            self.state = 36
            self.match(mCParser.ID)
            self.state = 37
            self.match(mCParser.LP)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==mCParser.INT or _la==mCParser.FLOAT:
                self.state = 38
                self.param_list()


            self.state = 41
            self.match(mCParser.RP)
            self.state = 42
            self.match(mCParser.LB)
            self.state = 43
            self.func_body()
            self.state = 44
            self.match(mCParser.RB)
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
            return mCParser.RULE_one_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOne_param" ):
                return visitor.visitOne_param(self)
            else:
                return visitor.visitChildren(self)




    def one_param(self):

        localctx = mCParser.One_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_one_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.type_stmt()

            self.state = 47
            self.match(mCParser.ID)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mCParser.CM:
                self.state = 48
                self.match(mCParser.CM)
                self.state = 49
                self.match(mCParser.ID)
                self.state = 54
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
                return self.getTypedRuleContexts(mCParser.One_paramContext)
            else:
                return self.getTypedRuleContext(mCParser.One_paramContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(mCParser.SM)
            else:
                return self.getToken(mCParser.SM, i)

        def getRuleIndex(self):
            return mCParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = mCParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.one_param()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mCParser.SM:
                self.state = 56
                self.match(mCParser.SM)
                self.state = 57
                self.one_param()
                self.state = 62
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = mCParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_func_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << mCParser.INT) | (1 << mCParser.FLOAT) | (1 << mCParser.RETURN) | (1 << mCParser.ID))) != 0):
                self.state = 65
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [mCParser.INT, mCParser.FLOAT]:
                    self.state = 63
                    self.var_dec()
                    pass
                elif token in [mCParser.RETURN, mCParser.ID]:
                    self.state = 64
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 69
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = mCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 70
                self.assignment()
                pass

            elif la_ == 2:
                self.state = 71
                self.call()
                pass

            elif la_ == 3:
                self.state = 72
                self.return_stmt()
                pass


            self.state = 75
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = mCParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(mCParser.ID)
            self.state = 78
            self.match(mCParser.EQ)
            self.state = 79
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = mCParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(mCParser.ID)
            self.state = 82
            self.match(mCParser.LP)
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << mCParser.INTLIT) | (1 << mCParser.FLOATLIT) | (1 << mCParser.LB) | (1 << mCParser.ID))) != 0):
                self.state = 83
                self.exp(0)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==mCParser.CM:
                    self.state = 84
                    self.match(mCParser.CM)
                    self.state = 85
                    self.exp(0)
                    self.state = 90
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 93
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = mCParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(mCParser.RETURN)
            self.state = 96
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
            return self.getToken(mCParser.LB, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mCParser.ExpContext)
            else:
                return self.getTypedRuleContext(mCParser.ExpContext,i)


        def RB(self):
            return self.getToken(mCParser.RB, 0)

        def INTLIT(self):
            return self.getToken(mCParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(mCParser.FLOATLIT, 0)

        def ID(self):
            return self.getToken(mCParser.ID, 0)

        def call(self):
            return self.getTypedRuleContext(mCParser.CallContext,0)


        def MUL(self):
            return self.getToken(mCParser.MUL, 0)

        def DIV(self):
            return self.getToken(mCParser.DIV, 0)

        def SUB(self):
            return self.getToken(mCParser.SUB, 0)

        def ADD(self):
            return self.getToken(mCParser.ADD, 0)

        def getRuleIndex(self):
            return mCParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mCParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 99
                self.match(mCParser.LB)
                self.state = 100
                self.exp(0)
                self.state = 101
                self.match(mCParser.RB)
                pass

            elif la_ == 2:
                self.state = 103
                self.match(mCParser.INTLIT)
                pass

            elif la_ == 3:
                self.state = 104
                self.match(mCParser.FLOATLIT)
                pass

            elif la_ == 4:
                self.state = 105
                self.match(mCParser.ID)
                pass

            elif la_ == 5:
                self.state = 106
                self.call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 121
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = mCParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 109
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 110
                        self.match(mCParser.MUL)
                        self.state = 111
                        self.exp(9)
                        pass

                    elif la_ == 2:
                        localctx = mCParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 112
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 113
                        self.match(mCParser.DIV)
                        self.state = 114
                        self.exp(8)
                        pass

                    elif la_ == 3:
                        localctx = mCParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 115
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 116
                        self.match(mCParser.SUB)
                        self.state = 117
                        self.exp(7)
                        pass

                    elif la_ == 4:
                        localctx = mCParser.ExpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 118
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 119
                        self.match(mCParser.ADD)
                        self.state = 120
                        self.exp(5)
                        pass

             
                self.state = 125
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
            return self.getToken(mCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(mCParser.FLOAT, 0)

        def getRuleIndex(self):
            return mCParser.RULE_type_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_stmt" ):
                return visitor.visitType_stmt(self)
            else:
                return visitor.visitChildren(self)




    def type_stmt(self):

        localctx = mCParser.Type_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
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
        self._predicates[10] = self.exp_sempred
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
         




