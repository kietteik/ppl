# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\30")
        buf.write("\u00b2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\5")
        buf.write("\20c\n\20\3\20\3\20\3\20\7\20h\n\20\f\20\16\20k\13\20")
        buf.write("\3\21\3\21\7\21o\n\21\f\21\16\21r\13\21\3\21\6\21u\n\21")
        buf.write("\r\21\16\21v\5\21y\n\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u0081\n\22\3\23\6\23\u0084\n\23\r\23\16\23\u0085")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\7\32\u0098\n\32\f\32\16\32\u009b")
        buf.write("\13\32\3\32\6\32\u009e\n\32\r\32\16\32\u009f\5\32\u00a2")
        buf.write("\n\32\3\33\3\33\6\33\u00a6\n\33\r\33\16\33\u00a7\3\34")
        buf.write("\3\34\5\34\u00ac\n\34\3\34\6\34\u00af\n\34\r\34\16\34")
        buf.write("\u00b0\2\2\35\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\2\61\2\63\2\65\2\67\2\3\2\7\3\2\63;\5\2\13\f")
        buf.write("\17\17\"\"\4\2C\\c|\3\2\62;\4\2GGgg\2\u00bc\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\39\3\2\2\2")
        buf.write("\5=\3\2\2\2\7C\3\2\2\2\tJ\3\2\2\2\13L\3\2\2\2\rN\3\2\2")
        buf.write("\2\17P\3\2\2\2\21R\3\2\2\2\23T\3\2\2\2\25V\3\2\2\2\27")
        buf.write("X\3\2\2\2\31Z\3\2\2\2\33\\\3\2\2\2\35^\3\2\2\2\37b\3\2")
        buf.write("\2\2!x\3\2\2\2#z\3\2\2\2%\u0083\3\2\2\2\'\u0089\3\2\2")
        buf.write("\2)\u008b\3\2\2\2+\u008d\3\2\2\2-\u008f\3\2\2\2/\u0091")
        buf.write("\3\2\2\2\61\u0093\3\2\2\2\63\u00a1\3\2\2\2\65\u00a3\3")
        buf.write("\2\2\2\67\u00a9\3\2\2\29:\7k\2\2:;\7p\2\2;<\7v\2\2<\4")
        buf.write("\3\2\2\2=>\7h\2\2>?\7n\2\2?@\7q\2\2@A\7c\2\2AB\7v\2\2")
        buf.write("B\6\3\2\2\2CD\7t\2\2DE\7g\2\2EF\7v\2\2FG\7w\2\2GH\7t\2")
        buf.write("\2HI\7p\2\2I\b\3\2\2\2JK\7}\2\2K\n\3\2\2\2LM\7\177\2\2")
        buf.write("M\f\3\2\2\2NO\7=\2\2O\16\3\2\2\2PQ\7.\2\2Q\20\3\2\2\2")
        buf.write("RS\7?\2\2S\22\3\2\2\2TU\7*\2\2U\24\3\2\2\2VW\7+\2\2W\26")
        buf.write("\3\2\2\2XY\7-\2\2Y\30\3\2\2\2Z[\7/\2\2[\32\3\2\2\2\\]")
        buf.write("\7,\2\2]\34\3\2\2\2^_\7\61\2\2_\36\3\2\2\2`c\7a\2\2ac")
        buf.write("\5/\30\2b`\3\2\2\2ba\3\2\2\2ci\3\2\2\2dh\7a\2\2eh\5/\30")
        buf.write("\2fh\5\61\31\2gd\3\2\2\2ge\3\2\2\2gf\3\2\2\2hk\3\2\2\2")
        buf.write("ig\3\2\2\2ij\3\2\2\2j \3\2\2\2ki\3\2\2\2lp\t\2\2\2mo\5")
        buf.write("\61\31\2nm\3\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2qy\3\2")
        buf.write("\2\2rp\3\2\2\2su\7\62\2\2ts\3\2\2\2uv\3\2\2\2vt\3\2\2")
        buf.write("\2vw\3\2\2\2wy\3\2\2\2xl\3\2\2\2xt\3\2\2\2y\"\3\2\2\2")
        buf.write("z\u0080\5\63\32\2{|\5\65\33\2|}\5\67\34\2}\u0081\3\2\2")
        buf.write("\2~\u0081\5\65\33\2\177\u0081\5\67\34\2\u0080{\3\2\2\2")
        buf.write("\u0080~\3\2\2\2\u0080\177\3\2\2\2\u0081$\3\2\2\2\u0082")
        buf.write("\u0084\t\3\2\2\u0083\u0082\3\2\2\2\u0084\u0085\3\2\2\2")
        buf.write("\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087\3")
        buf.write("\2\2\2\u0087\u0088\b\23\2\2\u0088&\3\2\2\2\u0089\u008a")
        buf.write("\13\2\2\2\u008a(\3\2\2\2\u008b\u008c\13\2\2\2\u008c*\3")
        buf.write("\2\2\2\u008d\u008e\13\2\2\2\u008e,\3\2\2\2\u008f\u0090")
        buf.write("\13\2\2\2\u0090.\3\2\2\2\u0091\u0092\t\4\2\2\u0092\60")
        buf.write("\3\2\2\2\u0093\u0094\t\5\2\2\u0094\62\3\2\2\2\u0095\u0099")
        buf.write("\t\2\2\2\u0096\u0098\5\61\31\2\u0097\u0096\3\2\2\2\u0098")
        buf.write("\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u00a2\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009e\7")
        buf.write("\62\2\2\u009d\u009c\3\2\2\2\u009e\u009f\3\2\2\2\u009f")
        buf.write("\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a2\3\2\2\2")
        buf.write("\u00a1\u0095\3\2\2\2\u00a1\u009d\3\2\2\2\u00a2\64\3\2")
        buf.write("\2\2\u00a3\u00a5\7\60\2\2\u00a4\u00a6\5\61\31\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a5\3\2\2\2")
        buf.write("\u00a7\u00a8\3\2\2\2\u00a8\66\3\2\2\2\u00a9\u00ab\t\6")
        buf.write("\2\2\u00aa\u00ac\7/\2\2\u00ab\u00aa\3\2\2\2\u00ab\u00ac")
        buf.write("\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00af\5\61\31\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00ae\3\2\2\2")
        buf.write("\u00b0\u00b1\3\2\2\2\u00b18\3\2\2\2\21\2bgipvx\u0080\u0085")
        buf.write("\u0099\u009f\u00a1\u00a7\u00ab\u00b0\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    FLOAT = 2
    RETURN = 3
    LB = 4
    RB = 5
    SM = 6
    CM = 7
    EQ = 8
    LP = 9
    RP = 10
    ADD = 11
    SUB = 12
    MUL = 13
    DIV = 14
    ID = 15
    INTLIT = 16
    FLOATLIT = 17
    WS = 18
    ERROR_CHAR = 19
    UNCLOSE_STRING = 20
    ILLEGAL_ESCAPE = 21
    UNTERMINATED_COMMENT = 22

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'return'", "'{'", "'}'", "';'", "','", 
            "'='", "'('", "')'", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "RETURN", "LB", "RB", "SM", "CM", "EQ", "LP", 
            "RP", "ADD", "SUB", "MUL", "DIV", "ID", "INTLIT", "FLOATLIT", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "INT", "FLOAT", "RETURN", "LB", "RB", "SM", "CM", "EQ", 
                  "LP", "RP", "ADD", "SUB", "MUL", "DIV", "ID", "INTLIT", 
                  "FLOATLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT", "ALPHA", "DIGIT", "INT_PART", 
                  "DEC_PART", "EXP_PART" ]

    grammarFileName = "BKIT.g4"

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


