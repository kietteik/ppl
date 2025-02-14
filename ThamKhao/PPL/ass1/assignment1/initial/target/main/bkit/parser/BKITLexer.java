// Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKITLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ADD=1, FADD=2, SUB=3, FSUB=4, MUL=5, FMUL=6, DIV=7, FDIV=8, MOD=9, NOT=10, 
		AND=11, OR=12, EQUAL=13, NOTEQUAL=14, LESS=15, GREATER=16, LESSEQUAL=17, 
		GREATEREQUAL=18, FNOTEQUAL=19, FLESS=20, FGREATER=21, FLESSEQUAL=22, FGREATEREQUAL=23, 
		KEY_BODY=24, KEY_BREAK=25, KEY_CONTINUE=26, KEY_DO=27, KEY_ELSE=28, KEY_ELSEIF=29, 
		KEY_ENDBODY=30, KEY_ENDIF=31, KEY_ENDFOR=32, KEY_ENDWHILE=33, KEY_FOR=34, 
		KEY_FUNCTION=35, KEY_IF=36, KEY_PARAMETER=37, KEY_RETURN=38, KEY_THEN=39, 
		KEY_VAR=40, KEY_WHILE=41, LSB=42, RSB=43, LP=44, RP=45, CL=46, DOT=47, 
		CM=48, SM=49, ASSIGN=50, INTLIT=51, DECIMAL=52, HEX=53, OCTAL=54, FLOATLIT=55, 
		BOOLLIT=56, STRINGLIT=57, ID=58, COMMENT=59, WS=60, UNCLOSE_STRING=61, 
		ILLEGAL_ESCAPE=62, ERROR_CHAR=63;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"LOWERCASE", "UPPERCASE", "NUMBER", "UNDERSCORE", "ADD", "FADD", "SUB", 
			"FSUB", "MUL", "FMUL", "DIV", "FDIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
			"NOTEQUAL", "LESS", "GREATER", "LESSEQUAL", "GREATEREQUAL", "FNOTEQUAL", 
			"FLESS", "FGREATER", "FLESSEQUAL", "FGREATEREQUAL", "KEY_BODY", "KEY_BREAK", 
			"KEY_CONTINUE", "KEY_DO", "KEY_ELSE", "KEY_ELSEIF", "KEY_ENDBODY", "KEY_ENDIF", 
			"KEY_ENDFOR", "KEY_ENDWHILE", "KEY_FOR", "KEY_FUNCTION", "KEY_IF", "KEY_PARAMETER", 
			"KEY_RETURN", "KEY_THEN", "KEY_VAR", "KEY_WHILE", "KEY_TRUE", "KEY_FALSE", 
			"LSB", "RSB", "LP", "RP", "CL", "DOT", "CM", "SM", "ASSIGN", "INTLIT", 
			"DECIMAL", "HEX", "OCTAL", "FLOATLIT", "BOOLLIT", "STRINGLIT", "ID", 
			"COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STR_CHAR", "ESC_SEQ", 
			"ESC_ILLEGAL", "ERROR_CHAR"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", "'\\'", "'/'", "'%'", 
			"'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
			"'=/='", "'<.'", "'>.'", "'<=.'", "'>=.'", "'Body'", "'Break'", "'Continue'", 
			"'Do'", "'Else'", "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
			"'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", 
			"'While'", "'['", "']'", "'('", "')'", "':'", "'.'", "','", "';'", "'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ADD", "FADD", "SUB", "FSUB", "MUL", "FMUL", "DIV", "FDIV", "MOD", 
			"NOT", "AND", "OR", "EQUAL", "NOTEQUAL", "LESS", "GREATER", "LESSEQUAL", 
			"GREATEREQUAL", "FNOTEQUAL", "FLESS", "FGREATER", "FLESSEQUAL", "FGREATEREQUAL", 
			"KEY_BODY", "KEY_BREAK", "KEY_CONTINUE", "KEY_DO", "KEY_ELSE", "KEY_ELSEIF", 
			"KEY_ENDBODY", "KEY_ENDIF", "KEY_ENDFOR", "KEY_ENDWHILE", "KEY_FOR", 
			"KEY_FUNCTION", "KEY_IF", "KEY_PARAMETER", "KEY_RETURN", "KEY_THEN", 
			"KEY_VAR", "KEY_WHILE", "LSB", "RSB", "LP", "RP", "CL", "DOT", "CM", 
			"SM", "ASSIGN", "INTLIT", "DECIMAL", "HEX", "OCTAL", "FLOATLIT", "BOOLLIT", 
			"STRINGLIT", "ID", "COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
			"ERROR_CHAR"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public BKITLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "BKIT.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A\u0234\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3"+
		"\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20"+
		"\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25"+
		"\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31"+
		"\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35"+
		"\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37"+
		"\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3"+
		"#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3&\3&\3"+
		"&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3"+
		")\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3"+
		"-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3"+
		"\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3"+
		"\67\38\38\39\39\3:\3:\3:\5:\u016c\n:\3;\6;\u016f\n;\r;\16;\u0170\3<\3"+
		"<\3<\3<\6<\u0177\n<\r<\16<\u0178\3=\3=\3=\6=\u017e\n=\r=\16=\u017f\3>"+
		"\6>\u0183\n>\r>\16>\u0184\3>\3>\7>\u0189\n>\f>\16>\u018c\13>\7>\u018e"+
		"\n>\f>\16>\u0191\13>\3>\3>\7>\u0195\n>\f>\16>\u0198\13>\3>\6>\u019b\n"+
		">\r>\16>\u019c\6>\u019f\n>\r>\16>\u01a0\3>\6>\u01a4\n>\r>\16>\u01a5\3"+
		">\3>\7>\u01aa\n>\f>\16>\u01ad\13>\6>\u01af\n>\r>\16>\u01b0\3>\3>\7>\u01b5"+
		"\n>\f>\16>\u01b8\13>\3>\6>\u01bb\n>\r>\16>\u01bc\7>\u01bf\n>\f>\16>\u01c2"+
		"\13>\3>\6>\u01c5\n>\r>\16>\u01c6\3>\3>\7>\u01cb\n>\f>\16>\u01ce\13>\6"+
		">\u01d0\n>\r>\16>\u01d1\3>\3>\7>\u01d6\n>\f>\16>\u01d9\13>\3>\6>\u01dc"+
		"\n>\r>\16>\u01dd\6>\u01e0\n>\r>\16>\u01e1\5>\u01e4\n>\3?\3?\5?\u01e8\n"+
		"?\3@\3@\7@\u01ec\n@\f@\16@\u01ef\13@\3@\3@\3A\3A\3A\3A\3A\7A\u01f8\nA"+
		"\fA\16A\u01fb\13A\3B\3B\3B\3B\7B\u0201\nB\fB\16B\u0204\13B\3B\3B\3B\3"+
		"B\3B\3C\6C\u020c\nC\rC\16C\u020d\3C\3C\3D\3D\7D\u0214\nD\fD\16D\u0217"+
		"\13D\3D\5D\u021a\nD\3E\3E\7E\u021e\nE\fE\16E\u0221\13E\3E\3E\3F\3F\3F"+
		"\3F\5F\u0229\nF\3G\3G\3G\3H\3H\3H\5H\u0231\nH\3I\3I\3\u0202\2J\3\2\5\2"+
		"\7\2\t\2\13\3\r\4\17\5\21\6\23\7\25\b\27\t\31\n\33\13\35\f\37\r!\16#\17"+
		"%\20\'\21)\22+\23-\24/\25\61\26\63\27\65\30\67\319\32;\33=\34?\35A\36"+
		"C\37E G!I\"K#M$O%Q&S\'U(W)Y*[+]\2_\2a,c-e.g/i\60k\61m\62o\63q\64s\65u"+
		"\66w\67y8{9}:\177;\u0081<\u0083=\u0085>\u0087?\u0089@\u008b\2\u008d\2"+
		"\u008f\2\u0091A\3\2\20\3\2c|\3\2C\\\3\2\62;\4\2ZZzz\3\2CH\4\2QQqq\3\2"+
		"\629\4\2GGgg\4\2--//\5\2\13\f\17\17\"\"\3\3\f\f\6\2\f\f$$))^^\n\2$$))"+
		"^^ddhhppttvv\3\2^^\2\u0251\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21"+
		"\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2"+
		"\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3"+
		"\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3"+
		"\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3"+
		"\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2"+
		"\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2"+
		"Y\3\2\2\2\2[\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3"+
		"\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2"+
		"\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3"+
		"\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2"+
		"\2\u0091\3\2\2\2\3\u0093\3\2\2\2\5\u0095\3\2\2\2\7\u0097\3\2\2\2\t\u0099"+
		"\3\2\2\2\13\u009b\3\2\2\2\r\u009d\3\2\2\2\17\u00a0\3\2\2\2\21\u00a2\3"+
		"\2\2\2\23\u00a5\3\2\2\2\25\u00a7\3\2\2\2\27\u00aa\3\2\2\2\31\u00ac\3\2"+
		"\2\2\33\u00ae\3\2\2\2\35\u00b0\3\2\2\2\37\u00b2\3\2\2\2!\u00b5\3\2\2\2"+
		"#\u00b8\3\2\2\2%\u00bb\3\2\2\2\'\u00be\3\2\2\2)\u00c0\3\2\2\2+\u00c2\3"+
		"\2\2\2-\u00c5\3\2\2\2/\u00c8\3\2\2\2\61\u00cc\3\2\2\2\63\u00cf\3\2\2\2"+
		"\65\u00d2\3\2\2\2\67\u00d6\3\2\2\29\u00da\3\2\2\2;\u00df\3\2\2\2=\u00e5"+
		"\3\2\2\2?\u00ee\3\2\2\2A\u00f1\3\2\2\2C\u00f6\3\2\2\2E\u00fd\3\2\2\2G"+
		"\u0105\3\2\2\2I\u010b\3\2\2\2K\u0112\3\2\2\2M\u011b\3\2\2\2O\u011f\3\2"+
		"\2\2Q\u0128\3\2\2\2S\u012b\3\2\2\2U\u0135\3\2\2\2W\u013c\3\2\2\2Y\u0141"+
		"\3\2\2\2[\u0145\3\2\2\2]\u014b\3\2\2\2_\u0150\3\2\2\2a\u0156\3\2\2\2c"+
		"\u0158\3\2\2\2e\u015a\3\2\2\2g\u015c\3\2\2\2i\u015e\3\2\2\2k\u0160\3\2"+
		"\2\2m\u0162\3\2\2\2o\u0164\3\2\2\2q\u0166\3\2\2\2s\u016b\3\2\2\2u\u016e"+
		"\3\2\2\2w\u0172\3\2\2\2y\u017a\3\2\2\2{\u01e3\3\2\2\2}\u01e7\3\2\2\2\177"+
		"\u01e9\3\2\2\2\u0081\u01f2\3\2\2\2\u0083\u01fc\3\2\2\2\u0085\u020b\3\2"+
		"\2\2\u0087\u0211\3\2\2\2\u0089\u021b\3\2\2\2\u008b\u0228\3\2\2\2\u008d"+
		"\u022a\3\2\2\2\u008f\u0230\3\2\2\2\u0091\u0232\3\2\2\2\u0093\u0094\t\2"+
		"\2\2\u0094\4\3\2\2\2\u0095\u0096\t\3\2\2\u0096\6\3\2\2\2\u0097\u0098\t"+
		"\4\2\2\u0098\b\3\2\2\2\u0099\u009a\7a\2\2\u009a\n\3\2\2\2\u009b\u009c"+
		"\7-\2\2\u009c\f\3\2\2\2\u009d\u009e\7-\2\2\u009e\u009f\7\60\2\2\u009f"+
		"\16\3\2\2\2\u00a0\u00a1\7/\2\2\u00a1\20\3\2\2\2\u00a2\u00a3\7/\2\2\u00a3"+
		"\u00a4\7\60\2\2\u00a4\22\3\2\2\2\u00a5\u00a6\7,\2\2\u00a6\24\3\2\2\2\u00a7"+
		"\u00a8\7,\2\2\u00a8\u00a9\7\60\2\2\u00a9\26\3\2\2\2\u00aa\u00ab\7^\2\2"+
		"\u00ab\30\3\2\2\2\u00ac\u00ad\7\61\2\2\u00ad\32\3\2\2\2\u00ae\u00af\7"+
		"\'\2\2\u00af\34\3\2\2\2\u00b0\u00b1\7#\2\2\u00b1\36\3\2\2\2\u00b2\u00b3"+
		"\7(\2\2\u00b3\u00b4\7(\2\2\u00b4 \3\2\2\2\u00b5\u00b6\7~\2\2\u00b6\u00b7"+
		"\7~\2\2\u00b7\"\3\2\2\2\u00b8\u00b9\7?\2\2\u00b9\u00ba\7?\2\2\u00ba$\3"+
		"\2\2\2\u00bb\u00bc\7#\2\2\u00bc\u00bd\7?\2\2\u00bd&\3\2\2\2\u00be\u00bf"+
		"\7>\2\2\u00bf(\3\2\2\2\u00c0\u00c1\7@\2\2\u00c1*\3\2\2\2\u00c2\u00c3\7"+
		">\2\2\u00c3\u00c4\7?\2\2\u00c4,\3\2\2\2\u00c5\u00c6\7@\2\2\u00c6\u00c7"+
		"\7?\2\2\u00c7.\3\2\2\2\u00c8\u00c9\7?\2\2\u00c9\u00ca\7\61\2\2\u00ca\u00cb"+
		"\7?\2\2\u00cb\60\3\2\2\2\u00cc\u00cd\7>\2\2\u00cd\u00ce\7\60\2\2\u00ce"+
		"\62\3\2\2\2\u00cf\u00d0\7@\2\2\u00d0\u00d1\7\60\2\2\u00d1\64\3\2\2\2\u00d2"+
		"\u00d3\7>\2\2\u00d3\u00d4\7?\2\2\u00d4\u00d5\7\60\2\2\u00d5\66\3\2\2\2"+
		"\u00d6\u00d7\7@\2\2\u00d7\u00d8\7?\2\2\u00d8\u00d9\7\60\2\2\u00d98\3\2"+
		"\2\2\u00da\u00db\7D\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd\7f\2\2\u00dd\u00de"+
		"\7{\2\2\u00de:\3\2\2\2\u00df\u00e0\7D\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2"+
		"\7g\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7m\2\2\u00e4<\3\2\2\2\u00e5\u00e6"+
		"\7E\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7v\2\2\u00e9"+
		"\u00ea\7k\2\2\u00ea\u00eb\7p\2\2\u00eb\u00ec\7w\2\2\u00ec\u00ed\7g\2\2"+
		"\u00ed>\3\2\2\2\u00ee\u00ef\7F\2\2\u00ef\u00f0\7q\2\2\u00f0@\3\2\2\2\u00f1"+
		"\u00f2\7G\2\2\u00f2\u00f3\7n\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5\7g\2\2"+
		"\u00f5B\3\2\2\2\u00f6\u00f7\7G\2\2\u00f7\u00f8\7n\2\2\u00f8\u00f9\7u\2"+
		"\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7K\2\2\u00fb\u00fc\7h\2\2\u00fcD\3\2"+
		"\2\2\u00fd\u00fe\7G\2\2\u00fe\u00ff\7p\2\2\u00ff\u0100\7f\2\2\u0100\u0101"+
		"\7D\2\2\u0101\u0102\7q\2\2\u0102\u0103\7f\2\2\u0103\u0104\7{\2\2\u0104"+
		"F\3\2\2\2\u0105\u0106\7G\2\2\u0106\u0107\7p\2\2\u0107\u0108\7f\2\2\u0108"+
		"\u0109\7K\2\2\u0109\u010a\7h\2\2\u010aH\3\2\2\2\u010b\u010c\7G\2\2\u010c"+
		"\u010d\7p\2\2\u010d\u010e\7f\2\2\u010e\u010f\7H\2\2\u010f\u0110\7q\2\2"+
		"\u0110\u0111\7t\2\2\u0111J\3\2\2\2\u0112\u0113\7G\2\2\u0113\u0114\7p\2"+
		"\2\u0114\u0115\7f\2\2\u0115\u0116\7Y\2\2\u0116\u0117\7j\2\2\u0117\u0118"+
		"\7k\2\2\u0118\u0119\7n\2\2\u0119\u011a\7g\2\2\u011aL\3\2\2\2\u011b\u011c"+
		"\7H\2\2\u011c\u011d\7q\2\2\u011d\u011e\7t\2\2\u011eN\3\2\2\2\u011f\u0120"+
		"\7H\2\2\u0120\u0121\7w\2\2\u0121\u0122\7p\2\2\u0122\u0123\7e\2\2\u0123"+
		"\u0124\7v\2\2\u0124\u0125\7k\2\2\u0125\u0126\7q\2\2\u0126\u0127\7p\2\2"+
		"\u0127P\3\2\2\2\u0128\u0129\7K\2\2\u0129\u012a\7h\2\2\u012aR\3\2\2\2\u012b"+
		"\u012c\7R\2\2\u012c\u012d\7c\2\2\u012d\u012e\7t\2\2\u012e\u012f\7c\2\2"+
		"\u012f\u0130\7o\2\2\u0130\u0131\7g\2\2\u0131\u0132\7v\2\2\u0132\u0133"+
		"\7g\2\2\u0133\u0134\7t\2\2\u0134T\3\2\2\2\u0135\u0136\7T\2\2\u0136\u0137"+
		"\7g\2\2\u0137\u0138\7v\2\2\u0138\u0139\7w\2\2\u0139\u013a\7t\2\2\u013a"+
		"\u013b\7p\2\2\u013bV\3\2\2\2\u013c\u013d\7V\2\2\u013d\u013e\7j\2\2\u013e"+
		"\u013f\7g\2\2\u013f\u0140\7p\2\2\u0140X\3\2\2\2\u0141\u0142\7X\2\2\u0142"+
		"\u0143\7c\2\2\u0143\u0144\7t\2\2\u0144Z\3\2\2\2\u0145\u0146\7Y\2\2\u0146"+
		"\u0147\7j\2\2\u0147\u0148\7k\2\2\u0148\u0149\7n\2\2\u0149\u014a\7g\2\2"+
		"\u014a\\\3\2\2\2\u014b\u014c\7V\2\2\u014c\u014d\7t\2\2\u014d\u014e\7w"+
		"\2\2\u014e\u014f\7g\2\2\u014f^\3\2\2\2\u0150\u0151\7H\2\2\u0151\u0152"+
		"\7c\2\2\u0152\u0153\7n\2\2\u0153\u0154\7u\2\2\u0154\u0155\7g\2\2\u0155"+
		"`\3\2\2\2\u0156\u0157\7]\2\2\u0157b\3\2\2\2\u0158\u0159\7_\2\2\u0159d"+
		"\3\2\2\2\u015a\u015b\7*\2\2\u015bf\3\2\2\2\u015c\u015d\7+\2\2\u015dh\3"+
		"\2\2\2\u015e\u015f\7<\2\2\u015fj\3\2\2\2\u0160\u0161\7\60\2\2\u0161l\3"+
		"\2\2\2\u0162\u0163\7.\2\2\u0163n\3\2\2\2\u0164\u0165\7=\2\2\u0165p\3\2"+
		"\2\2\u0166\u0167\7?\2\2\u0167r\3\2\2\2\u0168\u016c\5u;\2\u0169\u016c\5"+
		"w<\2\u016a\u016c\5y=\2\u016b\u0168\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016a"+
		"\3\2\2\2\u016ct\3\2\2\2\u016d\u016f\5\7\4\2\u016e\u016d\3\2\2\2\u016f"+
		"\u0170\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171v\3\2\2\2"+
		"\u0172\u0173\7\62\2\2\u0173\u0176\t\5\2\2\u0174\u0177\5\7\4\2\u0175\u0177"+
		"\t\6\2\2\u0176\u0174\3\2\2\2\u0176\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178"+
		"\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179x\3\2\2\2\u017a\u017b\7\62\2\2"+
		"\u017b\u017d\t\7\2\2\u017c\u017e\t\b\2\2\u017d\u017c\3\2\2\2\u017e\u017f"+
		"\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u0180\3\2\2\2\u0180z\3\2\2\2\u0181"+
		"\u0183\5\7\4\2\u0182\u0181\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0182\3\2"+
		"\2\2\u0184\u0185\3\2\2\2\u0185\u018f\3\2\2\2\u0186\u018a\5k\66\2\u0187"+
		"\u0189\5\7\4\2\u0188\u0187\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188\3\2"+
		"\2\2\u018a\u018b\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2\u018d"+
		"\u0186\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3\2"+
		"\2\2\u0190\u019e\3\2\2\2\u0191\u018f\3\2\2\2\u0192\u0196\t\t\2\2\u0193"+
		"\u0195\t\n\2\2\u0194\u0193\3\2\2\2\u0195\u0198\3\2\2\2\u0196\u0194\3\2"+
		"\2\2\u0196\u0197\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0199"+
		"\u019b\5\7\4\2\u019a\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019a\3\2"+
		"\2\2\u019c\u019d\3\2\2\2\u019d\u019f\3\2\2\2\u019e\u0192\3\2\2\2\u019f"+
		"\u01a0\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01e4\3\2"+
		"\2\2\u01a2\u01a4\5\7\4\2\u01a3\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5"+
		"\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01ae\3\2\2\2\u01a7\u01ab\5k"+
		"\66\2\u01a8\u01aa\5\7\4\2\u01a9\u01a8\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab"+
		"\u01a9\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2"+
		"\2\2\u01ae\u01a7\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0"+
		"\u01b1\3\2\2\2\u01b1\u01c0\3\2\2\2\u01b2\u01b6\t\t\2\2\u01b3\u01b5\t\n"+
		"\2\2\u01b4\u01b3\3\2\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6"+
		"\u01b7\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01bb\5\7"+
		"\4\2\u01ba\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bc"+
		"\u01bd\3\2\2\2\u01bd\u01bf\3\2\2\2\u01be\u01b2\3\2\2\2\u01bf\u01c2\3\2"+
		"\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01e4\3\2\2\2\u01c2"+
		"\u01c0\3\2\2\2\u01c3\u01c5\5\7\4\2\u01c4\u01c3\3\2\2\2\u01c5\u01c6\3\2"+
		"\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01cf\3\2\2\2\u01c8"+
		"\u01cc\5k\66\2\u01c9\u01cb\5\7\4\2\u01ca\u01c9\3\2\2\2\u01cb\u01ce\3\2"+
		"\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce"+
		"\u01cc\3\2\2\2\u01cf\u01c8\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01cf\3\2"+
		"\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01df\3\2\2\2\u01d3\u01d7\t\t\2\2\u01d4"+
		"\u01d6\t\n\2\2\u01d5\u01d4\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3\2"+
		"\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2\u01da"+
		"\u01dc\5\7\4\2\u01db\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01db\3\2"+
		"\2\2\u01dd\u01de\3\2\2\2\u01de\u01e0\3\2\2\2\u01df\u01d3\3\2\2\2\u01e0"+
		"\u01e1\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e4\3\2"+
		"\2\2\u01e3\u0182\3\2\2\2\u01e3\u01a3\3\2\2\2\u01e3\u01c4\3\2\2\2\u01e4"+
		"|\3\2\2\2\u01e5\u01e8\5]/\2\u01e6\u01e8\5_\60\2\u01e7\u01e5\3\2\2\2\u01e7"+
		"\u01e6\3\2\2\2\u01e8~\3\2\2\2\u01e9\u01ed\7$\2\2\u01ea\u01ec\5\u008bF"+
		"\2\u01eb\u01ea\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee"+
		"\3\2\2\2\u01ee\u01f0\3\2\2\2\u01ef\u01ed\3\2\2\2\u01f0\u01f1\7$\2\2\u01f1"+
		"\u0080\3\2\2\2\u01f2\u01f9\5\3\2\2\u01f3\u01f8\5\5\3\2\u01f4\u01f8\5\3"+
		"\2\2\u01f5\u01f8\5\t\5\2\u01f6\u01f8\5\7\4\2\u01f7\u01f3\3\2\2\2\u01f7"+
		"\u01f4\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f6\3\2\2\2\u01f8\u01fb\3\2"+
		"\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u0082\3\2\2\2\u01fb"+
		"\u01f9\3\2\2\2\u01fc\u01fd\7,\2\2\u01fd\u01fe\7,\2\2\u01fe\u0202\3\2\2"+
		"\2\u01ff\u0201\13\2\2\2\u0200\u01ff\3\2\2\2\u0201\u0204\3\2\2\2\u0202"+
		"\u0203\3\2\2\2\u0202\u0200\3\2\2\2\u0203\u0205\3\2\2\2\u0204\u0202\3\2"+
		"\2\2\u0205\u0206\7,\2\2\u0206\u0207\7,\2\2\u0207\u0208\3\2\2\2\u0208\u0209"+
		"\bB\2\2\u0209\u0084\3\2\2\2\u020a\u020c\t\13\2\2\u020b\u020a\3\2\2\2\u020c"+
		"\u020d\3\2\2\2\u020d\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020f\3\2"+
		"\2\2\u020f\u0210\bC\2\2\u0210\u0086\3\2\2\2\u0211\u0215\7$\2\2\u0212\u0214"+
		"\5\u008bF\2\u0213\u0212\3\2\2\2\u0214\u0217\3\2\2\2\u0215\u0213\3\2\2"+
		"\2\u0215\u0216\3\2\2\2\u0216\u0219\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u021a"+
		"\t\f\2\2\u0219\u0218\3\2\2\2\u021a\u0088\3\2\2\2\u021b\u021f\7$\2\2\u021c"+
		"\u021e\5\u008bF\2\u021d\u021c\3\2\2\2\u021e\u0221\3\2\2\2\u021f\u021d"+
		"\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0222\3\2\2\2\u0221\u021f\3\2\2\2\u0222"+
		"\u0223\5\u008fH\2\u0223\u008a\3\2\2\2\u0224\u0229\n\r\2\2\u0225\u0229"+
		"\5\u008dG\2\u0226\u0227\7)\2\2\u0227\u0229\7$\2\2\u0228\u0224\3\2\2\2"+
		"\u0228\u0225\3\2\2\2\u0228\u0226\3\2\2\2\u0229\u008c\3\2\2\2\u022a\u022b"+
		"\7^\2\2\u022b\u022c\t\16\2\2\u022c\u008e\3\2\2\2\u022d\u022e\7^\2\2\u022e"+
		"\u0231\n\16\2\2\u022f\u0231\n\17\2\2\u0230\u022d\3\2\2\2\u0230\u022f\3"+
		"\2\2\2\u0231\u0090\3\2\2\2\u0232\u0233\13\2\2\2\u0233\u0092\3\2\2\2&\2"+
		"\u016b\u0170\u0176\u0178\u017f\u0184\u018a\u018f\u0196\u019c\u01a0\u01a5"+
		"\u01ab\u01b0\u01b6\u01bc\u01c0\u01c6\u01cc\u01d1\u01d7\u01dd\u01e1\u01e3"+
		"\u01e7\u01ed\u01f7\u01f9\u0202\u020d\u0215\u0219\u021f\u0228\u0230\3\b"+
		"\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}