# Generated from /Users/kietteik/Documents/BKU_Stored/HK1_2020-2021/PPL/Asm3/initial_run/src/main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0261\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\3\2\3\2\5\2\u00b4\n\2\3\2\6\2\u00b7")
        buf.write("\n\2\r\2\16\2\u00b8\3\3\6\3\u00bc\n\3\r\3\16\3\u00bd\3")
        buf.write("\3\3\3\7\3\u00c2\n\3\f\3\16\3\u00c5\13\3\3\3\6\3\u00c8")
        buf.write("\n\3\r\3\16\3\u00c9\3\3\3\3\7\3\u00ce\n\3\f\3\16\3\u00d1")
        buf.write("\13\3\3\3\7\3\u00d4\n\3\f\3\16\3\u00d7\13\3\5\3\u00d9")
        buf.write("\n\3\3\4\3\4\3\4\5\4\u00de\n\4\3\5\3\5\3\5\3\5\3\5\7\5")
        buf.write("\u00e5\n\5\f\5\16\5\u00e8\13\5\3\6\3\6\3\6\3\6\7\6\u00ee")
        buf.write("\n\6\f\6\16\6\u00f1\13\6\3\7\3\7\3\7\7\7\u00f6\n\7\f\7")
        buf.write("\16\7\u00f9\13\7\5\7\u00fb\n\7\3\b\3\b\5\b\u00ff\n\b\3")
        buf.write("\t\3\t\3\t\3\n\3\n\7\n\u0106\n\n\f\n\16\n\u0109\13\n\3")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3#\3#")
        buf.write("\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,")
        buf.write("\3,\3-\7-\u0165\n-\f-\16-\u0168\13-\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\39\39\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3<\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\3=\3=\3=\3>\3>\3>\3>\3>\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3@\3@\3@\3@\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\3C\3C\3D\3D\3D\3")
        buf.write("D\3E\3E\3E\3E\3E\3E\3E\3E\3E\3F\3F\3F\3G\3G\3G\3G\3G\3")
        buf.write("G\3G\3G\3G\3G\3H\3H\3H\3H\3H\3H\3H\3I\3I\3I\3I\3I\3J\3")
        buf.write("J\3J\3J\3K\3K\3K\3K\3K\3K\3L\3L\3L\3L\3L\3M\3M\3M\3M\3")
        buf.write("M\3M\3N\3N\3N\3N\3N\3N\3O\3O\3O\3O\3O\7O\u0210\nO\fO\16")
        buf.write("O\u0213\13O\3P\3P\3P\3P\7P\u0219\nP\fP\16P\u021c\13P\3")
        buf.write("P\3P\3P\3P\3P\3Q\6Q\u0224\nQ\rQ\16Q\u0225\3Q\3Q\3R\3R")
        buf.write("\3R\3R\5R\u022e\nR\3S\3S\3S\3S\3S\5S\u0235\nS\3T\3T\3")
        buf.write("T\3T\3T\5T\u023c\nT\3U\3U\3V\3V\7V\u0242\nV\fV\16V\u0245")
        buf.write("\13V\3V\5V\u0248\nV\3V\3V\3W\3W\7W\u024e\nW\fW\16W\u0251")
        buf.write("\13W\3W\3W\3W\3X\3X\3X\3X\7X\u025a\nX\fX\16X\u025d\13")
        buf.write("X\3X\3X\3X\4\u0107\u021a\2Y\3\2\5\3\7\4\t\2\13\2\r\2\17")
        buf.write("\5\21\2\23\6\25\7\27\b\31\t\33\n\35\13\37\f!\r#\16%\17")
        buf.write("\'\20)\21+\22-\23/\24\61\25\63\26\65\27\67\309\31;\32")
        buf.write("=\33?\34A\35C\36E\37G I!K\"M#O$Q%S&U\'W(Y\2[\2]\2_\2a")
        buf.write("\2c\2e\2g\2i\2k\2m\2o\2q\2s)u*w+y,{-}.\177/\u0081\60\u0083")
        buf.write("\61\u0085\62\u0087\63\u0089\64\u008b\65\u008d\66\u008f")
        buf.write("\67\u00918\u00939\u0095:\u0097;\u0099<\u009b=\u009d>\u009f")
        buf.write("?\u00a1@\u00a3\2\u00a5\2\u00a7\2\u00a9A\u00abB\u00adC")
        buf.write("\u00afD\3\2\26\4\2GGgg\4\2--//\4\2ZZzz\4\2\63;CH\3\2C")
        buf.write("H\4\2QQqq\3\2\639\3\2\629\3\2\63;\t\2))^^ddhhppttvv\3")
        buf.write("\2\"\"\3\2\62;\3\2c|\3\2C\\\3\2))\3\2$$\5\2\13\f\17\17")
        buf.write("\"\"\7\2\n\n\f\f$$))^^\3\2,,\4\3\f\f\17\17\2\u026d\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\17\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2")
        buf.write("\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\3\u00b1\3\2\2")
        buf.write("\2\5\u00bb\3\2\2\2\7\u00dd\3\2\2\2\t\u00df\3\2\2\2\13")
        buf.write("\u00e9\3\2\2\2\r\u00fa\3\2\2\2\17\u00fe\3\2\2\2\21\u0100")
        buf.write("\3\2\2\2\23\u0103\3\2\2\2\25\u010d\3\2\2\2\27\u0110\3")
        buf.write("\2\2\2\31\u0112\3\2\2\2\33\u0114\3\2\2\2\35\u0117\3\2")
        buf.write("\2\2\37\u0119\3\2\2\2!\u011c\3\2\2\2#\u011e\3\2\2\2%\u0121")
        buf.write("\3\2\2\2\'\u0123\3\2\2\2)\u0125\3\2\2\2+\u0128\3\2\2\2")
        buf.write("-\u012b\3\2\2\2/\u012e\3\2\2\2\61\u0131\3\2\2\2\63\u0133")
        buf.write("\3\2\2\2\65\u0135\3\2\2\2\67\u0138\3\2\2\29\u013b\3\2")
        buf.write("\2\2;\u013f\3\2\2\2=\u0142\3\2\2\2?\u0145\3\2\2\2A\u0149")
        buf.write("\3\2\2\2C\u014d\3\2\2\2E\u014f\3\2\2\2G\u0151\3\2\2\2")
        buf.write("I\u0153\3\2\2\2K\u0155\3\2\2\2M\u0157\3\2\2\2O\u0159\3")
        buf.write("\2\2\2Q\u015b\3\2\2\2S\u015d\3\2\2\2U\u015f\3\2\2\2W\u0161")
        buf.write("\3\2\2\2Y\u0166\3\2\2\2[\u0169\3\2\2\2]\u016b\3\2\2\2")
        buf.write("_\u016d\3\2\2\2a\u016f\3\2\2\2c\u0171\3\2\2\2e\u0174\3")
        buf.write("\2\2\2g\u0177\3\2\2\2i\u017a\3\2\2\2k\u017d\3\2\2\2m\u0180")
        buf.write("\3\2\2\2o\u0182\3\2\2\2q\u0184\3\2\2\2s\u0188\3\2\2\2")
        buf.write("u\u018d\3\2\2\2w\u0193\3\2\2\2y\u019c\3\2\2\2{\u019f\3")
        buf.write("\2\2\2}\u01a4\3\2\2\2\177\u01ab\3\2\2\2\u0081\u01b3\3")
        buf.write("\2\2\2\u0083\u01b9\3\2\2\2\u0085\u01c0\3\2\2\2\u0087\u01c9")
        buf.write("\3\2\2\2\u0089\u01cd\3\2\2\2\u008b\u01d6\3\2\2\2\u008d")
        buf.write("\u01d9\3\2\2\2\u008f\u01e3\3\2\2\2\u0091\u01ea\3\2\2\2")
        buf.write("\u0093\u01ef\3\2\2\2\u0095\u01f3\3\2\2\2\u0097\u01f9\3")
        buf.write("\2\2\2\u0099\u01fe\3\2\2\2\u009b\u0204\3\2\2\2\u009d\u020a")
        buf.write("\3\2\2\2\u009f\u0214\3\2\2\2\u00a1\u0223\3\2\2\2\u00a3")
        buf.write("\u022d\3\2\2\2\u00a5\u0234\3\2\2\2\u00a7\u023b\3\2\2\2")
        buf.write("\u00a9\u023d\3\2\2\2\u00ab\u023f\3\2\2\2\u00ad\u024b\3")
        buf.write("\2\2\2\u00af\u0255\3\2\2\2\u00b1\u00b3\t\2\2\2\u00b2\u00b4")
        buf.write("\t\3\2\2\u00b3\u00b2\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4")
        buf.write("\u00b6\3\2\2\2\u00b5\u00b7\5[.\2\u00b6\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b8\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2")
        buf.write("\u00b9\4\3\2\2\2\u00ba\u00bc\5[.\2\u00bb\u00ba\3\2\2\2")
        buf.write("\u00bc\u00bd\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00be\3")
        buf.write("\2\2\2\u00be\u00d8\3\2\2\2\u00bf\u00c3\5M\'\2\u00c0\u00c2")
        buf.write("\5[.\2\u00c1\u00c0\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00d9\3\2\2\2\u00c5")
        buf.write("\u00c3\3\2\2\2\u00c6\u00c8\5\3\2\2\u00c7\u00c6\3\2\2\2")
        buf.write("\u00c8\u00c9\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3")
        buf.write("\2\2\2\u00ca\u00d9\3\2\2\2\u00cb\u00cf\5M\'\2\u00cc\u00ce")
        buf.write("\5[.\2\u00cd\u00cc\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd")
        buf.write("\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d5\3\2\2\2\u00d1")
        buf.write("\u00cf\3\2\2\2\u00d2\u00d4\5\3\2\2\u00d3\u00d2\3\2\2\2")
        buf.write("\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3")
        buf.write("\2\2\2\u00d6\u00d9\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00bf")
        buf.write("\3\2\2\2\u00d8\u00c7\3\2\2\2\u00d8\u00cb\3\2\2\2\u00d9")
        buf.write("\6\3\2\2\2\u00da\u00de\5\t\5\2\u00db\u00de\5\13\6\2\u00dc")
        buf.write("\u00de\5\r\7\2\u00dd\u00da\3\2\2\2\u00dd\u00db\3\2\2\2")
        buf.write("\u00dd\u00dc\3\2\2\2\u00de\b\3\2\2\2\u00df\u00e0\7\62")
        buf.write("\2\2\u00e0\u00e1\t\4\2\2\u00e1\u00e6\t\5\2\2\u00e2\u00e5")
        buf.write("\5[.\2\u00e3\u00e5\t\6\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e3")
        buf.write("\3\2\2\2\u00e5\u00e8\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6")
        buf.write("\u00e7\3\2\2\2\u00e7\n\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9")
        buf.write("\u00ea\7\62\2\2\u00ea\u00eb\t\7\2\2\u00eb\u00ef\t\b\2")
        buf.write("\2\u00ec\u00ee\t\t\2\2\u00ed\u00ec\3\2\2\2\u00ee\u00f1")
        buf.write("\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0")
        buf.write("\f\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00fb\7\62\2\2\u00f3")
        buf.write("\u00f7\t\n\2\2\u00f4\u00f6\5[.\2\u00f5\u00f4\3\2\2\2\u00f6")
        buf.write("\u00f9\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2")
        buf.write("\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00fa\u00f2\3")
        buf.write("\2\2\2\u00fa\u00f3\3\2\2\2\u00fb\16\3\2\2\2\u00fc\u00ff")
        buf.write("\5\u0097L\2\u00fd\u00ff\5\u0099M\2\u00fe\u00fc\3\2\2\2")
        buf.write("\u00fe\u00fd\3\2\2\2\u00ff\20\3\2\2\2\u0100\u0101\7^\2")
        buf.write("\2\u0101\u0102\t\13\2\2\u0102\22\3\2\2\2\u0103\u0107\5")
        buf.write("o8\2\u0104\u0106\5\u00a3R\2\u0105\u0104\3\2\2\2\u0106")
        buf.write("\u0109\3\2\2\2\u0107\u0108\3\2\2\2\u0107\u0105\3\2\2\2")
        buf.write("\u0108\u010a\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u010b\5")
        buf.write("o8\2\u010b\u010c\b\n\2\2\u010c\24\3\2\2\2\u010d\u010e")
        buf.write("\7-\2\2\u010e\u010f\7\60\2\2\u010f\26\3\2\2\2\u0110\u0111")
        buf.write("\7-\2\2\u0111\30\3\2\2\2\u0112\u0113\7/\2\2\u0113\32\3")
        buf.write("\2\2\2\u0114\u0115\7/\2\2\u0115\u0116\7\60\2\2\u0116\34")
        buf.write("\3\2\2\2\u0117\u0118\7,\2\2\u0118\36\3\2\2\2\u0119\u011a")
        buf.write("\7,\2\2\u011a\u011b\7\60\2\2\u011b \3\2\2\2\u011c\u011d")
        buf.write("\7^\2\2\u011d\"\3\2\2\2\u011e\u011f\7^\2\2\u011f\u0120")
        buf.write("\7\60\2\2\u0120$\3\2\2\2\u0121\u0122\7\'\2\2\u0122&\3")
        buf.write("\2\2\2\u0123\u0124\7#\2\2\u0124(\3\2\2\2\u0125\u0126\7")
        buf.write("(\2\2\u0126\u0127\7(\2\2\u0127*\3\2\2\2\u0128\u0129\7")
        buf.write("~\2\2\u0129\u012a\7~\2\2\u012a,\3\2\2\2\u012b\u012c\7")
        buf.write("?\2\2\u012c\u012d\7?\2\2\u012d.\3\2\2\2\u012e\u012f\7")
        buf.write("#\2\2\u012f\u0130\7?\2\2\u0130\60\3\2\2\2\u0131\u0132")
        buf.write("\7>\2\2\u0132\62\3\2\2\2\u0133\u0134\7@\2\2\u0134\64\3")
        buf.write("\2\2\2\u0135\u0136\7>\2\2\u0136\u0137\7?\2\2\u0137\66")
        buf.write("\3\2\2\2\u0138\u0139\7@\2\2\u0139\u013a\7?\2\2\u013a8")
        buf.write("\3\2\2\2\u013b\u013c\7?\2\2\u013c\u013d\7\61\2\2\u013d")
        buf.write("\u013e\7?\2\2\u013e:\3\2\2\2\u013f\u0140\7>\2\2\u0140")
        buf.write("\u0141\7\60\2\2\u0141<\3\2\2\2\u0142\u0143\7@\2\2\u0143")
        buf.write("\u0144\7\60\2\2\u0144>\3\2\2\2\u0145\u0146\7>\2\2\u0146")
        buf.write("\u0147\7?\2\2\u0147\u0148\7\60\2\2\u0148@\3\2\2\2\u0149")
        buf.write("\u014a\7@\2\2\u014a\u014b\7?\2\2\u014b\u014c\7\60\2\2")
        buf.write("\u014cB\3\2\2\2\u014d\u014e\7]\2\2\u014eD\3\2\2\2\u014f")
        buf.write("\u0150\7_\2\2\u0150F\3\2\2\2\u0151\u0152\7*\2\2\u0152")
        buf.write("H\3\2\2\2\u0153\u0154\7+\2\2\u0154J\3\2\2\2\u0155\u0156")
        buf.write("\7<\2\2\u0156L\3\2\2\2\u0157\u0158\7\60\2\2\u0158N\3\2")
        buf.write("\2\2\u0159\u015a\7.\2\2\u015aP\3\2\2\2\u015b\u015c\7=")
        buf.write("\2\2\u015cR\3\2\2\2\u015d\u015e\7}\2\2\u015eT\3\2\2\2")
        buf.write("\u015f\u0160\7\177\2\2\u0160V\3\2\2\2\u0161\u0162\7?\2")
        buf.write("\2\u0162X\3\2\2\2\u0163\u0165\t\f\2\2\u0164\u0163\3\2")
        buf.write("\2\2\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167")
        buf.write("\3\2\2\2\u0167Z\3\2\2\2\u0168\u0166\3\2\2\2\u0169\u016a")
        buf.write("\t\r\2\2\u016a\\\3\2\2\2\u016b\u016c\t\16\2\2\u016c^\3")
        buf.write("\2\2\2\u016d\u016e\t\17\2\2\u016e`\3\2\2\2\u016f\u0170")
        buf.write("\7a\2\2\u0170b\3\2\2\2\u0171\u0172\7^\2\2\u0172\u0173")
        buf.write("\7d\2\2\u0173d\3\2\2\2\u0174\u0175\7^\2\2\u0175\u0176")
        buf.write("\7h\2\2\u0176f\3\2\2\2\u0177\u0178\7^\2\2\u0178\u0179")
        buf.write("\7t\2\2\u0179h\3\2\2\2\u017a\u017b\7^\2\2\u017b\u017c")
        buf.write("\7p\2\2\u017cj\3\2\2\2\u017d\u017e\7^\2\2\u017e\u017f")
        buf.write("\7v\2\2\u017fl\3\2\2\2\u0180\u0181\t\20\2\2\u0181n\3\2")
        buf.write("\2\2\u0182\u0183\t\21\2\2\u0183p\3\2\2\2\u0184\u0185\7")
        buf.write("^\2\2\u0185\u0186\7^\2\2\u0186\u0187\7$\2\2\u0187r\3\2")
        buf.write("\2\2\u0188\u0189\7D\2\2\u0189\u018a\7q\2\2\u018a\u018b")
        buf.write("\7f\2\2\u018b\u018c\7{\2\2\u018ct\3\2\2\2\u018d\u018e")
        buf.write("\7D\2\2\u018e\u018f\7t\2\2\u018f\u0190\7g\2\2\u0190\u0191")
        buf.write("\7c\2\2\u0191\u0192\7m\2\2\u0192v\3\2\2\2\u0193\u0194")
        buf.write("\7E\2\2\u0194\u0195\7q\2\2\u0195\u0196\7p\2\2\u0196\u0197")
        buf.write("\7v\2\2\u0197\u0198\7k\2\2\u0198\u0199\7p\2\2\u0199\u019a")
        buf.write("\7w\2\2\u019a\u019b\7g\2\2\u019bx\3\2\2\2\u019c\u019d")
        buf.write("\7F\2\2\u019d\u019e\7q\2\2\u019ez\3\2\2\2\u019f\u01a0")
        buf.write("\7G\2\2\u01a0\u01a1\7n\2\2\u01a1\u01a2\7u\2\2\u01a2\u01a3")
        buf.write("\7g\2\2\u01a3|\3\2\2\2\u01a4\u01a5\7G\2\2\u01a5\u01a6")
        buf.write("\7n\2\2\u01a6\u01a7\7u\2\2\u01a7\u01a8\7g\2\2\u01a8\u01a9")
        buf.write("\7K\2\2\u01a9\u01aa\7h\2\2\u01aa~\3\2\2\2\u01ab\u01ac")
        buf.write("\7G\2\2\u01ac\u01ad\7p\2\2\u01ad\u01ae\7f\2\2\u01ae\u01af")
        buf.write("\7D\2\2\u01af\u01b0\7q\2\2\u01b0\u01b1\7f\2\2\u01b1\u01b2")
        buf.write("\7{\2\2\u01b2\u0080\3\2\2\2\u01b3\u01b4\7G\2\2\u01b4\u01b5")
        buf.write("\7p\2\2\u01b5\u01b6\7f\2\2\u01b6\u01b7\7K\2\2\u01b7\u01b8")
        buf.write("\7h\2\2\u01b8\u0082\3\2\2\2\u01b9\u01ba\7G\2\2\u01ba\u01bb")
        buf.write("\7p\2\2\u01bb\u01bc\7f\2\2\u01bc\u01bd\7H\2\2\u01bd\u01be")
        buf.write("\7q\2\2\u01be\u01bf\7t\2\2\u01bf\u0084\3\2\2\2\u01c0\u01c1")
        buf.write("\7G\2\2\u01c1\u01c2\7p\2\2\u01c2\u01c3\7f\2\2\u01c3\u01c4")
        buf.write("\7Y\2\2\u01c4\u01c5\7j\2\2\u01c5\u01c6\7k\2\2\u01c6\u01c7")
        buf.write("\7n\2\2\u01c7\u01c8\7g\2\2\u01c8\u0086\3\2\2\2\u01c9\u01ca")
        buf.write("\7H\2\2\u01ca\u01cb\7q\2\2\u01cb\u01cc\7t\2\2\u01cc\u0088")
        buf.write("\3\2\2\2\u01cd\u01ce\7H\2\2\u01ce\u01cf\7w\2\2\u01cf\u01d0")
        buf.write("\7p\2\2\u01d0\u01d1\7e\2\2\u01d1\u01d2\7v\2\2\u01d2\u01d3")
        buf.write("\7k\2\2\u01d3\u01d4\7q\2\2\u01d4\u01d5\7p\2\2\u01d5\u008a")
        buf.write("\3\2\2\2\u01d6\u01d7\7K\2\2\u01d7\u01d8\7h\2\2\u01d8\u008c")
        buf.write("\3\2\2\2\u01d9\u01da\7R\2\2\u01da\u01db\7c\2\2\u01db\u01dc")
        buf.write("\7t\2\2\u01dc\u01dd\7c\2\2\u01dd\u01de\7o\2\2\u01de\u01df")
        buf.write("\7g\2\2\u01df\u01e0\7v\2\2\u01e0\u01e1\7g\2\2\u01e1\u01e2")
        buf.write("\7t\2\2\u01e2\u008e\3\2\2\2\u01e3\u01e4\7T\2\2\u01e4\u01e5")
        buf.write("\7g\2\2\u01e5\u01e6\7v\2\2\u01e6\u01e7\7w\2\2\u01e7\u01e8")
        buf.write("\7t\2\2\u01e8\u01e9\7p\2\2\u01e9\u0090\3\2\2\2\u01ea\u01eb")
        buf.write("\7V\2\2\u01eb\u01ec\7j\2\2\u01ec\u01ed\7g\2\2\u01ed\u01ee")
        buf.write("\7p\2\2\u01ee\u0092\3\2\2\2\u01ef\u01f0\7X\2\2\u01f0\u01f1")
        buf.write("\7c\2\2\u01f1\u01f2\7t\2\2\u01f2\u0094\3\2\2\2\u01f3\u01f4")
        buf.write("\7Y\2\2\u01f4\u01f5\7j\2\2\u01f5\u01f6\7k\2\2\u01f6\u01f7")
        buf.write("\7n\2\2\u01f7\u01f8\7g\2\2\u01f8\u0096\3\2\2\2\u01f9\u01fa")
        buf.write("\7V\2\2\u01fa\u01fb\7t\2\2\u01fb\u01fc\7w\2\2\u01fc\u01fd")
        buf.write("\7g\2\2\u01fd\u0098\3\2\2\2\u01fe\u01ff\7H\2\2\u01ff\u0200")
        buf.write("\7c\2\2\u0200\u0201\7n\2\2\u0201\u0202\7u\2\2\u0202\u0203")
        buf.write("\7g\2\2\u0203\u009a\3\2\2\2\u0204\u0205\7G\2\2\u0205\u0206")
        buf.write("\7p\2\2\u0206\u0207\7f\2\2\u0207\u0208\7F\2\2\u0208\u0209")
        buf.write("\7q\2\2\u0209\u009c\3\2\2\2\u020a\u0211\5]/\2\u020b\u0210")
        buf.write("\5]/\2\u020c\u0210\5_\60\2\u020d\u0210\5a\61\2\u020e\u0210")
        buf.write("\5[.\2\u020f\u020b\3\2\2\2\u020f\u020c\3\2\2\2\u020f\u020d")
        buf.write("\3\2\2\2\u020f\u020e\3\2\2\2\u0210\u0213\3\2\2\2\u0211")
        buf.write("\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u009e\3\2\2\2")
        buf.write("\u0213\u0211\3\2\2\2\u0214\u0215\7,\2\2\u0215\u0216\7")
        buf.write(",\2\2\u0216\u021a\3\2\2\2\u0217\u0219\5\u00a7T\2\u0218")
        buf.write("\u0217\3\2\2\2\u0219\u021c\3\2\2\2\u021a\u021b\3\2\2\2")
        buf.write("\u021a\u0218\3\2\2\2\u021b\u021d\3\2\2\2\u021c\u021a\3")
        buf.write("\2\2\2\u021d\u021e\7,\2\2\u021e\u021f\7,\2\2\u021f\u0220")
        buf.write("\3\2\2\2\u0220\u0221\bP\3\2\u0221\u00a0\3\2\2\2\u0222")
        buf.write("\u0224\t\22\2\2\u0223\u0222\3\2\2\2\u0224\u0225\3\2\2")
        buf.write("\2\u0225\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0227")
        buf.write("\3\2\2\2\u0227\u0228\bQ\3\2\u0228\u00a2\3\2\2\2\u0229")
        buf.write("\u022e\n\23\2\2\u022a\u022e\5\21\t\2\u022b\u022c\7)\2")
        buf.write("\2\u022c\u022e\7$\2\2\u022d\u0229\3\2\2\2\u022d\u022a")
        buf.write("\3\2\2\2\u022d\u022b\3\2\2\2\u022e\u00a4\3\2\2\2\u022f")
        buf.write("\u0230\7^\2\2\u0230\u0235\n\13\2\2\u0231\u0235\7^\2\2")
        buf.write("\u0232\u0233\t\20\2\2\u0233\u0235\n\21\2\2\u0234\u022f")
        buf.write("\3\2\2\2\u0234\u0231\3\2\2\2\u0234\u0232\3\2\2\2\u0235")
        buf.write("\u00a6\3\2\2\2\u0236\u023c\n\24\2\2\u0237\u0238\t\24\2")
        buf.write("\2\u0238\u023c\n\24\2\2\u0239\u023a\t\24\2\2\u023a\u023c")
        buf.write("\7\2\2\3\u023b\u0236\3\2\2\2\u023b\u0237\3\2\2\2\u023b")
        buf.write("\u0239\3\2\2\2\u023c\u00a8\3\2\2\2\u023d\u023e\13\2\2")
        buf.write("\2\u023e\u00aa\3\2\2\2\u023f\u0243\7$\2\2\u0240\u0242")
        buf.write("\5\u00a3R\2\u0241\u0240\3\2\2\2\u0242\u0245\3\2\2\2\u0243")
        buf.write("\u0241\3\2\2\2\u0243\u0244\3\2\2\2\u0244\u0247\3\2\2\2")
        buf.write("\u0245\u0243\3\2\2\2\u0246\u0248\t\25\2\2\u0247\u0246")
        buf.write("\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u024a\bV\4\2\u024a")
        buf.write("\u00ac\3\2\2\2\u024b\u024f\7$\2\2\u024c\u024e\5\u00a3")
        buf.write("R\2\u024d\u024c\3\2\2\2\u024e\u0251\3\2\2\2\u024f\u024d")
        buf.write("\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u0252\3\2\2\2\u0251")
        buf.write("\u024f\3\2\2\2\u0252\u0253\5\u00a5S\2\u0253\u0254\bW\5")
        buf.write("\2\u0254\u00ae\3\2\2\2\u0255\u0256\7,\2\2\u0256\u0257")
        buf.write("\7,\2\2\u0257\u025b\3\2\2\2\u0258\u025a\5\u00a7T\2\u0259")
        buf.write("\u0258\3\2\2\2\u025a\u025d\3\2\2\2\u025b\u0259\3\2\2\2")
        buf.write("\u025b\u025c\3\2\2\2\u025c\u025e\3\2\2\2\u025d\u025b\3")
        buf.write("\2\2\2\u025e\u025f\7\2\2\3\u025f\u0260\bX\6\2\u0260\u00b0")
        buf.write("\3\2\2\2\37\2\u00b3\u00b8\u00bd\u00c3\u00c9\u00cf\u00d5")
        buf.write("\u00d8\u00dd\u00e4\u00e6\u00ef\u00f7\u00fa\u00fe\u0107")
        buf.write("\u0166\u020f\u0211\u021a\u0225\u022d\u0234\u023b\u0243")
        buf.write("\u0247\u024f\u025b\7\3\n\2\b\2\2\3V\3\3W\4\3X\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    FLOATLIT = 1
    INTLIT = 2
    BOOLLIT = 3
    STRING = 4
    ADDF = 5
    ADD = 6
    SUB = 7
    SUBF = 8
    MUL = 9
    MULF = 10
    DIV = 11
    DIVF = 12
    MOD = 13
    NOT = 14
    CONJ = 15
    DISJ = 16
    EQUAL = 17
    NEQUAL = 18
    LT = 19
    GT = 20
    LTE = 21
    GTE = 22
    NEQF = 23
    LTF = 24
    GTF = 25
    LTEF = 26
    GTEF = 27
    LSB = 28
    RSB = 29
    LP = 30
    RP = 31
    CL = 32
    DOT = 33
    CM = 34
    SM = 35
    LCB = 36
    RCB = 37
    ASSIGN = 38
    BODY = 39
    BREAK = 40
    CONTINUE = 41
    DO = 42
    ELSE = 43
    ELSEIF = 44
    ENDBODY = 45
    ENDIF = 46
    ENDFOR = 47
    ENDWHILE = 48
    FOR = 49
    FUNCTION = 50
    IF = 51
    PARAMETER = 52
    RETURN = 53
    THEN = 54
    VAR = 55
    WHILE = 56
    TRUE = 57
    FALSE = 58
    ENDDO = 59
    ID = 60
    COMMENT = 61
    WS = 62
    ERROR_CHAR = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    UNTERMINATED_COMMENT = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+.'", "'+'", "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", 
            "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'['", 
            "']'", "'('", "')'", "':'", "'.'", "','", "';'", "'{'", "'}'", 
            "'='", "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
            "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
            "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
            "'Var'", "'While'", "'True'", "'False'", "'EndDo'" ]

    symbolicNames = [ "<INVALID>",
            "FLOATLIT", "INTLIT", "BOOLLIT", "STRING", "ADDF", "ADD", "SUB", 
            "SUBF", "MUL", "MULF", "DIV", "DIVF", "MOD", "NOT", "CONJ", 
            "DISJ", "EQUAL", "NEQUAL", "LT", "GT", "LTE", "GTE", "NEQF", 
            "LTF", "GTF", "LTEF", "GTEF", "LSB", "RSB", "LP", "RP", "CL", 
            "DOT", "CM", "SM", "LCB", "RCB", "ASSIGN", "BODY", "BREAK", 
            "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
            "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", 
            "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", "ID", "COMMENT", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "EXPONENT", "FLOATLIT", "INTLIT", "HEX", "OCTAL", "DEC", 
                  "BOOLLIT", "ESC_SEQ", "STRING", "ADDF", "ADD", "SUB", 
                  "SUBF", "MUL", "MULF", "DIV", "DIVF", "MOD", "NOT", "CONJ", 
                  "DISJ", "EQUAL", "NEQUAL", "LT", "GT", "LTE", "GTE", "NEQF", 
                  "LTF", "GTF", "LTEF", "GTEF", "LSB", "RSB", "LP", "RP", 
                  "CL", "DOT", "CM", "SM", "LCB", "RCB", "ASSIGN", "SPACE", 
                  "NUMBER", "LOWER", "UPPER", "UNDERSCORE", "BACKSPACE", 
                  "FORMFEED", "CARRIAGE_RETURN", "NEWLINE", "HORIZONTAL_TAB", 
                  "SINGLE_QUOTE", "DOUBLE_QUOTE", "BACK_SLASH", "BODY", 
                  "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
                  "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", 
                  "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
                  "FALSE", "ENDDO", "ID", "COMMENT", "WS", "STR_CHAR", "ESC_ILLEGAL", 
                  "COMMENT_CHAR", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[8] = self.STRING_action 
            actions[84] = self.UNCLOSE_STRING_action 
            actions[85] = self.ILLEGAL_ESCAPE_action 
            actions[86] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             
            		y = str(self.text) 
            		possible = ['\n', '\r'] 
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1]) 
            		else: 
            			raise UncloseString(y[1:]) 
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             
            		y = str(self.text) 
            		raise IllegalEscape(y[1:]) 
            	
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise UnterminatedComment() 
     


