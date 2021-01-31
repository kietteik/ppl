# Generated from d:\Stu\Semester 3\Principles of Programming Languages\Tut\Tut3\test\PC_code\initial\src\main\mC\parser\mC.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\32")
        buf.write("\u00a5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\5\6\5A\n\5\r\5\16\5B\3\6\6\6F\n\6\r\6\16")
        buf.write("\6G\3\6\3\6\6\6L\n\6\r\6\16\6M\3\6\3\6\5\6R\n\6\3\6\3")
        buf.write("\6\3\6\5\6W\n\6\5\6Y\n\6\5\6[\n\6\3\6\6\6^\n\6\r\6\16")
        buf.write("\6_\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\7\27\u0092\n\27\f\27\16\27\u0095\13\27\3\30\6\30")
        buf.write("\u0098\n\30\r\30\16\30\u0099\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\2\2\35\3\2\5\2\7\2\t\3\13\4")
        buf.write("\r\5\17\6\21\7\23\b\25\t\27\n\31\13\33\f\35\r\37\16!\17")
        buf.write("#\20%\21\'\22)\23+\24-\25/\26\61\27\63\30\65\31\67\32")
        buf.write("\3\2\7\3\2c|\3\2\62;\4\2GGgg\4\2--//\5\2\13\f\16\17\"")
        buf.write("\"\2\u00ac\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\39\3\2\2\2\5;\3\2\2")
        buf.write("\2\7=\3\2\2\2\t@\3\2\2\2\13E\3\2\2\2\ra\3\2\2\2\17e\3")
        buf.write("\2\2\2\21k\3\2\2\2\23r\3\2\2\2\25t\3\2\2\2\27v\3\2\2\2")
        buf.write("\31x\3\2\2\2\33z\3\2\2\2\35|\3\2\2\2\37~\3\2\2\2!\u0080")
        buf.write("\3\2\2\2#\u0082\3\2\2\2%\u0084\3\2\2\2\'\u0086\3\2\2\2")
        buf.write(")\u0088\3\2\2\2+\u008a\3\2\2\2-\u008e\3\2\2\2/\u0097\3")
        buf.write("\2\2\2\61\u009d\3\2\2\2\63\u009f\3\2\2\2\65\u00a1\3\2")
        buf.write("\2\2\67\u00a3\3\2\2\29:\t\2\2\2:\4\3\2\2\2;<\t\3\2\2<")
        buf.write("\6\3\2\2\2=>\7\60\2\2>\b\3\2\2\2?A\5\5\3\2@?\3\2\2\2A")
        buf.write("B\3\2\2\2B@\3\2\2\2BC\3\2\2\2C\n\3\2\2\2DF\5\5\3\2ED\3")
        buf.write("\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HZ\3\2\2\2IK\5\7\4")
        buf.write("\2JL\5\5\3\2KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2N")
        buf.write("O\3\2\2\2OQ\t\4\2\2PR\t\5\2\2QP\3\2\2\2QR\3\2\2\2R[\3")
        buf.write("\2\2\2SY\5\7\4\2TV\t\4\2\2UW\t\5\2\2VU\3\2\2\2VW\3\2\2")
        buf.write("\2WY\3\2\2\2XS\3\2\2\2XT\3\2\2\2Y[\3\2\2\2ZI\3\2\2\2Z")
        buf.write("X\3\2\2\2[]\3\2\2\2\\^\5\5\3\2]\\\3\2\2\2^_\3\2\2\2_]")
        buf.write("\3\2\2\2_`\3\2\2\2`\f\3\2\2\2ab\7k\2\2bc\7p\2\2cd\7v\2")
        buf.write("\2d\16\3\2\2\2ef\7h\2\2fg\7n\2\2gh\7q\2\2hi\7c\2\2ij\7")
        buf.write("v\2\2j\20\3\2\2\2kl\7t\2\2lm\7g\2\2mn\7v\2\2no\7w\2\2")
        buf.write("op\7t\2\2pq\7p\2\2q\22\3\2\2\2rs\7}\2\2s\24\3\2\2\2tu")
        buf.write("\7\177\2\2u\26\3\2\2\2vw\7=\2\2w\30\3\2\2\2xy\7.\2\2y")
        buf.write("\32\3\2\2\2z{\7?\2\2{\34\3\2\2\2|}\7*\2\2}\36\3\2\2\2")
        buf.write("~\177\7+\2\2\177 \3\2\2\2\u0080\u0081\7-\2\2\u0081\"\3")
        buf.write("\2\2\2\u0082\u0083\7/\2\2\u0083$\3\2\2\2\u0084\u0085\7")
        buf.write(",\2\2\u0085&\3\2\2\2\u0086\u0087\7\61\2\2\u0087(\3\2\2")
        buf.write("\2\u0088\u0089\7<\2\2\u0089*\3\2\2\2\u008a\u008b\7X\2")
        buf.write("\2\u008b\u008c\7c\2\2\u008c\u008d\7t\2\2\u008d,\3\2\2")
        buf.write("\2\u008e\u0093\5\3\2\2\u008f\u0092\5\3\2\2\u0090\u0092")
        buf.write("\5\5\3\2\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2\2\u0092")
        buf.write("\u0095\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2")
        buf.write("\u0094.\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0098\t\6\2")
        buf.write("\2\u0097\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099\u0097")
        buf.write("\3\2\2\2\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2\u009b")
        buf.write("\u009c\b\30\2\2\u009c\60\3\2\2\2\u009d\u009e\13\2\2\2")
        buf.write("\u009e\62\3\2\2\2\u009f\u00a0\13\2\2\2\u00a0\64\3\2\2")
        buf.write("\2\u00a1\u00a2\13\2\2\2\u00a2\66\3\2\2\2\u00a3\u00a4\13")
        buf.write("\2\2\2\u00a48\3\2\2\2\16\2BGMQVXZ_\u0091\u0093\u0099\3")
        buf.write("\b\2\2")
        return buf.getvalue()


class mCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    FLOATLIT = 2
    INT = 3
    FLOAT = 4
    RETURN = 5
    LB = 6
    RB = 7
    SM = 8
    CM = 9
    EQ = 10
    LP = 11
    RP = 12
    ADD = 13
    SUB = 14
    MUL = 15
    DIV = 16
    COLON = 17
    VAR = 18
    ID = 19
    WS = 20
    ERROR_CHAR = 21
    UNCLOSE_STRING = 22
    ILLEGAL_ESCAPE = 23
    UNTERMINATED_COMMENT = 24

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'return'", "'{'", "'}'", "';'", "','", 
            "'='", "'('", "')'", "'+'", "'-'", "'*'", "'/'", "':'", "'Var'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "INT", "FLOAT", "RETURN", "LB", "RB", 
            "SM", "CM", "EQ", "LP", "RP", "ADD", "SUB", "MUL", "DIV", "COLON", 
            "VAR", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "LETTER", "NUMBER", "DOT", "INTLIT", "FLOATLIT", "INT", 
                  "FLOAT", "RETURN", "LB", "RB", "SM", "CM", "EQ", "LP", 
                  "RP", "ADD", "SUB", "MUL", "DIV", "COLON", "VAR", "ID", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

    grammarFileName = "mC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


