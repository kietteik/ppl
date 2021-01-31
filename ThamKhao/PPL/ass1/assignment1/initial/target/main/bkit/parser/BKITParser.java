// Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class BKITParser extends Parser {
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
	public static final int
		RULE_program = 0, RULE_listVarDeclar = 1, RULE_listFuncDeclar = 2, RULE_noNullListVarDeclar = 3, 
		RULE_noNullListFuncDeclar = 4, RULE_vardeclara = 5, RULE_listvar = 6, 
		RULE_var = 7, RULE_nonInitVar = 8, RULE_initVar = 9, RULE_varArrayIdentifier = 10, 
		RULE_var_index_operators = 11, RULE_literal = 12, RULE_funcdeclara = 13, 
		RULE_listparam = 14, RULE_param = 15, RULE_funcbody = 16, RULE_liststatements = 17, 
		RULE_noNullListStatements = 18, RULE_statement = 19, RULE_assigment = 20, 
		RULE_if_statement = 21, RULE_for_statement = 22, RULE_while_statement = 23, 
		RULE_do_while_statement = 24, RULE_break_statement = 25, RULE_continue_statement = 26, 
		RULE_call_statement = 27, RULE_return_statement = 28, RULE_exp = 29, RULE_exp1 = 30, 
		RULE_exp2 = 31, RULE_exp3 = 32, RULE_exp4 = 33, RULE_exp5 = 34, RULE_exp6 = 35, 
		RULE_exp7 = 36, RULE_element_exp = 37, RULE_index_operators = 38, RULE_func_call = 39, 
		RULE_listExp = 40, RULE_noNullListExp = 41;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "listVarDeclar", "listFuncDeclar", "noNullListVarDeclar", 
			"noNullListFuncDeclar", "vardeclara", "listvar", "var", "nonInitVar", 
			"initVar", "varArrayIdentifier", "var_index_operators", "literal", "funcdeclara", 
			"listparam", "param", "funcbody", "liststatements", "noNullListStatements", 
			"statement", "assigment", "if_statement", "for_statement", "while_statement", 
			"do_while_statement", "break_statement", "continue_statement", "call_statement", 
			"return_statement", "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
			"exp7", "element_exp", "index_operators", "func_call", "listExp", "noNullListExp"
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

	@Override
	public String getGrammarFileName() { return "BKIT.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BKITParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public ListVarDeclarContext listVarDeclar() {
			return getRuleContext(ListVarDeclarContext.class,0);
		}
		public ListFuncDeclarContext listFuncDeclar() {
			return getRuleContext(ListFuncDeclarContext.class,0);
		}
		public TerminalNode EOF() { return getToken(BKITParser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			listVarDeclar();
			setState(85);
			listFuncDeclar();
			setState(86);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ListVarDeclarContext extends ParserRuleContext {
		public NoNullListVarDeclarContext noNullListVarDeclar() {
			return getRuleContext(NoNullListVarDeclarContext.class,0);
		}
		public ListVarDeclarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listVarDeclar; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitListVarDeclar(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ListVarDeclarContext listVarDeclar() throws RecognitionException {
		ListVarDeclarContext _localctx = new ListVarDeclarContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_listVarDeclar);
		try {
			setState(90);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KEY_VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(88);
				noNullListVarDeclar();
				}
				break;
			case EOF:
			case KEY_FUNCTION:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ListFuncDeclarContext extends ParserRuleContext {
		public NoNullListFuncDeclarContext noNullListFuncDeclar() {
			return getRuleContext(NoNullListFuncDeclarContext.class,0);
		}
		public ListFuncDeclarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listFuncDeclar; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitListFuncDeclar(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ListFuncDeclarContext listFuncDeclar() throws RecognitionException {
		ListFuncDeclarContext _localctx = new ListFuncDeclarContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_listFuncDeclar);
		try {
			setState(94);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case KEY_FUNCTION:
				enterOuterAlt(_localctx, 1);
				{
				setState(92);
				noNullListFuncDeclar();
				}
				break;
			case EOF:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NoNullListVarDeclarContext extends ParserRuleContext {
		public VardeclaraContext vardeclara() {
			return getRuleContext(VardeclaraContext.class,0);
		}
		public NoNullListVarDeclarContext noNullListVarDeclar() {
			return getRuleContext(NoNullListVarDeclarContext.class,0);
		}
		public NoNullListVarDeclarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_noNullListVarDeclar; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitNoNullListVarDeclar(this);
			else return visitor.visitChildren(this);
		}
	}

	public final NoNullListVarDeclarContext noNullListVarDeclar() throws RecognitionException {
		NoNullListVarDeclarContext _localctx = new NoNullListVarDeclarContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_noNullListVarDeclar);
		try {
			setState(100);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(96);
				vardeclara();
				setState(97);
				noNullListVarDeclar();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(99);
				vardeclara();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NoNullListFuncDeclarContext extends ParserRuleContext {
		public FuncdeclaraContext funcdeclara() {
			return getRuleContext(FuncdeclaraContext.class,0);
		}
		public NoNullListFuncDeclarContext noNullListFuncDeclar() {
			return getRuleContext(NoNullListFuncDeclarContext.class,0);
		}
		public NoNullListFuncDeclarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_noNullListFuncDeclar; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitNoNullListFuncDeclar(this);
			else return visitor.visitChildren(this);
		}
	}

	public final NoNullListFuncDeclarContext noNullListFuncDeclar() throws RecognitionException {
		NoNullListFuncDeclarContext _localctx = new NoNullListFuncDeclarContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_noNullListFuncDeclar);
		try {
			setState(106);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(102);
				funcdeclara();
				setState(103);
				noNullListFuncDeclar();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(105);
				funcdeclara();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VardeclaraContext extends ParserRuleContext {
		public TerminalNode KEY_VAR() { return getToken(BKITParser.KEY_VAR, 0); }
		public TerminalNode CL() { return getToken(BKITParser.CL, 0); }
		public ListvarContext listvar() {
			return getRuleContext(ListvarContext.class,0);
		}
		public TerminalNode SM() { return getToken(BKITParser.SM, 0); }
		public VardeclaraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardeclara; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitVardeclara(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VardeclaraContext vardeclara() throws RecognitionException {
		VardeclaraContext _localctx = new VardeclaraContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_vardeclara);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(KEY_VAR);
			setState(109);
			match(CL);
			setState(110);
			listvar();
			setState(111);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ListvarContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public TerminalNode CM() { return getToken(BKITParser.CM, 0); }
		public ListvarContext listvar() {
			return getRuleContext(ListvarContext.class,0);
		}
		public ListvarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listvar; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitListvar(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ListvarContext listvar() throws RecognitionException {
		ListvarContext _localctx = new ListvarContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_listvar);
		try {
			setState(118);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(113);
				var();
				setState(114);
				match(CM);
				setState(115);
				listvar();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(117);
				var();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarContext extends ParserRuleContext {
		public NonInitVarContext nonInitVar() {
			return getRuleContext(NonInitVarContext.class,0);
		}
		public InitVarContext initVar() {
			return getRuleContext(InitVarContext.class,0);
		}
		public VarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitVar(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VarContext var() throws RecognitionException {
		VarContext _localctx = new VarContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_var);
		try {
			setState(122);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(120);
				nonInitVar();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(121);
				initVar();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NonInitVarContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public VarArrayIdentifierContext varArrayIdentifier() {
			return getRuleContext(VarArrayIdentifierContext.class,0);
		}
		public NonInitVarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nonInitVar; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitNonInitVar(this);
			else return visitor.visitChildren(this);
		}
	}

	public final NonInitVarContext nonInitVar() throws RecognitionException {
		NonInitVarContext _localctx = new NonInitVarContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_nonInitVar);
		try {
			setState(126);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(124);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(125);
				varArrayIdentifier();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class InitVarContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public VarArrayIdentifierContext varArrayIdentifier() {
			return getRuleContext(VarArrayIdentifierContext.class,0);
		}
		public InitVarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_initVar; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitInitVar(this);
			else return visitor.visitChildren(this);
		}
	}

	public final InitVarContext initVar() throws RecognitionException {
		InitVarContext _localctx = new InitVarContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_initVar);
		try {
			setState(135);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(128);
				match(ID);
				setState(129);
				match(ASSIGN);
				setState(130);
				literal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(131);
				varArrayIdentifier();
				setState(132);
				match(ASSIGN);
				setState(133);
				literal();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VarArrayIdentifierContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public Var_index_operatorsContext var_index_operators() {
			return getRuleContext(Var_index_operatorsContext.class,0);
		}
		public VarArrayIdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_varArrayIdentifier; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitVarArrayIdentifier(this);
			else return visitor.visitChildren(this);
		}
	}

	public final VarArrayIdentifierContext varArrayIdentifier() throws RecognitionException {
		VarArrayIdentifierContext _localctx = new VarArrayIdentifierContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_varArrayIdentifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			match(ID);
			setState(138);
			var_index_operators();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_index_operatorsContext extends ParserRuleContext {
		public TerminalNode LSB() { return getToken(BKITParser.LSB, 0); }
		public TerminalNode INTLIT() { return getToken(BKITParser.INTLIT, 0); }
		public TerminalNode RSB() { return getToken(BKITParser.RSB, 0); }
		public Var_index_operatorsContext var_index_operators() {
			return getRuleContext(Var_index_operatorsContext.class,0);
		}
		public Var_index_operatorsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_index_operators; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitVar_index_operators(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Var_index_operatorsContext var_index_operators() throws RecognitionException {
		Var_index_operatorsContext _localctx = new Var_index_operatorsContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_var_index_operators);
		try {
			setState(147);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(140);
				match(LSB);
				setState(141);
				match(INTLIT);
				setState(142);
				match(RSB);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(143);
				match(LSB);
				setState(144);
				match(INTLIT);
				setState(145);
				match(RSB);
				setState(146);
				var_index_operators();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode INTLIT() { return getToken(BKITParser.INTLIT, 0); }
		public TerminalNode FLOATLIT() { return getToken(BKITParser.FLOATLIT, 0); }
		public TerminalNode BOOLLIT() { return getToken(BKITParser.BOOLLIT, 0); }
		public TerminalNode STRINGLIT() { return getToken(BKITParser.STRINGLIT, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitLiteral(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(149);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INTLIT) | (1L << FLOATLIT) | (1L << BOOLLIT) | (1L << STRINGLIT))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncdeclaraContext extends ParserRuleContext {
		public TerminalNode KEY_FUNCTION() { return getToken(BKITParser.KEY_FUNCTION, 0); }
		public List<TerminalNode> CL() { return getTokens(BKITParser.CL); }
		public TerminalNode CL(int i) {
			return getToken(BKITParser.CL, i);
		}
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode KEY_PARAMETER() { return getToken(BKITParser.KEY_PARAMETER, 0); }
		public ListparamContext listparam() {
			return getRuleContext(ListparamContext.class,0);
		}
		public FuncbodyContext funcbody() {
			return getRuleContext(FuncbodyContext.class,0);
		}
		public FuncdeclaraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcdeclara; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitFuncdeclara(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FuncdeclaraContext funcdeclara() throws RecognitionException {
		FuncdeclaraContext _localctx = new FuncdeclaraContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_funcdeclara);
		try {
			setState(163);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(151);
				match(KEY_FUNCTION);
				setState(152);
				match(CL);
				setState(153);
				match(ID);
				setState(154);
				match(KEY_PARAMETER);
				setState(155);
				match(CL);
				setState(156);
				listparam();
				setState(157);
				funcbody();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(159);
				match(KEY_FUNCTION);
				setState(160);
				match(CL);
				setState(161);
				match(ID);
				setState(162);
				funcbody();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ListparamContext extends ParserRuleContext {
		public ParamContext param() {
			return getRuleContext(ParamContext.class,0);
		}
		public TerminalNode CM() { return getToken(BKITParser.CM, 0); }
		public ListparamContext listparam() {
			return getRuleContext(ListparamContext.class,0);
		}
		public ListparamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listparam; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitListparam(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ListparamContext listparam() throws RecognitionException {
		ListparamContext _localctx = new ListparamContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_listparam);
		try {
			setState(170);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(165);
				param();
				setState(166);
				match(CM);
				setState(167);
				listparam();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(169);
				param();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitParam(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncbodyContext extends ParserRuleContext {
		public TerminalNode KEY_BODY() { return getToken(BKITParser.KEY_BODY, 0); }
		public TerminalNode CL() { return getToken(BKITParser.CL, 0); }
		public ListstatementsContext liststatements() {
			return getRuleContext(ListstatementsContext.class,0);
		}
		public TerminalNode KEY_ENDBODY() { return getToken(BKITParser.KEY_ENDBODY, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public FuncbodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_funcbody; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitFuncbody(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FuncbodyContext funcbody() throws RecognitionException {
		FuncbodyContext _localctx = new FuncbodyContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_funcbody);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			match(KEY_BODY);
			setState(175);
			match(CL);
			setState(176);
			liststatements();
			setState(177);
			match(KEY_ENDBODY);
			setState(178);
			match(DOT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ListstatementsContext extends ParserRuleContext {
		public NoNullListStatementsContext noNullListStatements() {
			return getRuleContext(NoNullListStatementsContext.class,0);
		}
		public ListstatementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_liststatements; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitListstatements(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ListstatementsContext liststatements() throws RecognitionException {
		ListstatementsContext _localctx = new ListstatementsContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_liststatements);
		try {
			setState(182);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(180);
				noNullListStatements();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NoNullListStatementsContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public NoNullListStatementsContext noNullListStatements() {
			return getRuleContext(NoNullListStatementsContext.class,0);
		}
		public NoNullListStatementsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_noNullListStatements; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitNoNullListStatements(this);
			else return visitor.visitChildren(this);
		}
	}

	public final NoNullListStatementsContext noNullListStatements() throws RecognitionException {
		NoNullListStatementsContext _localctx = new NoNullListStatementsContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_noNullListStatements);
		try {
			setState(188);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(184);
				statement();
				setState(185);
				noNullListStatements();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(187);
				statement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public VardeclaraContext vardeclara() {
			return getRuleContext(VardeclaraContext.class,0);
		}
		public AssigmentContext assigment() {
			return getRuleContext(AssigmentContext.class,0);
		}
		public If_statementContext if_statement() {
			return getRuleContext(If_statementContext.class,0);
		}
		public For_statementContext for_statement() {
			return getRuleContext(For_statementContext.class,0);
		}
		public While_statementContext while_statement() {
			return getRuleContext(While_statementContext.class,0);
		}
		public Do_while_statementContext do_while_statement() {
			return getRuleContext(Do_while_statementContext.class,0);
		}
		public Break_statementContext break_statement() {
			return getRuleContext(Break_statementContext.class,0);
		}
		public Continue_statementContext continue_statement() {
			return getRuleContext(Continue_statementContext.class,0);
		}
		public Call_statementContext call_statement() {
			return getRuleContext(Call_statementContext.class,0);
		}
		public Return_statementContext return_statement() {
			return getRuleContext(Return_statementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_statement);
		try {
			setState(200);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(190);
				vardeclara();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(191);
				assigment();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(192);
				if_statement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(193);
				for_statement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(194);
				while_statement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(195);
				do_while_statement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(196);
				break_statement();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(197);
				continue_statement();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(198);
				call_statement();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(199);
				return_statement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssigmentContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(BKITParser.ASSIGN, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode SM() { return getToken(BKITParser.SM, 0); }
		public AssigmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assigment; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitAssigment(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AssigmentContext assigment() throws RecognitionException {
		AssigmentContext _localctx = new AssigmentContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_assigment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			var();
			setState(203);
			match(ASSIGN);
			setState(204);
			exp(0);
			setState(205);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_statementContext extends ParserRuleContext {
		public TerminalNode KEY_IF() { return getToken(BKITParser.KEY_IF, 0); }
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public List<TerminalNode> KEY_THEN() { return getTokens(BKITParser.KEY_THEN); }
		public TerminalNode KEY_THEN(int i) {
			return getToken(BKITParser.KEY_THEN, i);
		}
		public List<ListstatementsContext> liststatements() {
			return getRuleContexts(ListstatementsContext.class);
		}
		public ListstatementsContext liststatements(int i) {
			return getRuleContext(ListstatementsContext.class,i);
		}
		public TerminalNode KEY_ENDIF() { return getToken(BKITParser.KEY_ENDIF, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public List<TerminalNode> KEY_ELSEIF() { return getTokens(BKITParser.KEY_ELSEIF); }
		public TerminalNode KEY_ELSEIF(int i) {
			return getToken(BKITParser.KEY_ELSEIF, i);
		}
		public TerminalNode KEY_ELSE() { return getToken(BKITParser.KEY_ELSE, 0); }
		public If_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_statement; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitIf_statement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final If_statementContext if_statement() throws RecognitionException {
		If_statementContext _localctx = new If_statementContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_if_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(207);
			match(KEY_IF);
			setState(208);
			exp(0);
			setState(209);
			match(KEY_THEN);
			setState(210);
			liststatements();
			setState(218);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==KEY_ELSEIF) {
				{
				{
				setState(211);
				match(KEY_ELSEIF);
				setState(212);
				exp(0);
				setState(213);
				match(KEY_THEN);
				setState(214);
				liststatements();
				}
				}
				setState(220);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(223);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KEY_ELSE) {
				{
				setState(221);
				match(KEY_ELSE);
				setState(222);
				liststatements();
				}
			}

			setState(225);
			match(KEY_ENDIF);
			setState(226);
			match(DOT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class For_statementContext extends ParserRuleContext {
		public TerminalNode KEY_FOR() { return getToken(BKITParser.KEY_FOR, 0); }
		public TerminalNode LP() { return getToken(BKITParser.LP, 0); }
		public List<VarContext> var() {
			return getRuleContexts(VarContext.class);
		}
		public VarContext var(int i) {
			return getRuleContext(VarContext.class,i);
		}
		public List<TerminalNode> ASSIGN() { return getTokens(BKITParser.ASSIGN); }
		public TerminalNode ASSIGN(int i) {
			return getToken(BKITParser.ASSIGN, i);
		}
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public List<TerminalNode> CM() { return getTokens(BKITParser.CM); }
		public TerminalNode CM(int i) {
			return getToken(BKITParser.CM, i);
		}
		public TerminalNode RP() { return getToken(BKITParser.RP, 0); }
		public TerminalNode KEY_DO() { return getToken(BKITParser.KEY_DO, 0); }
		public ListstatementsContext liststatements() {
			return getRuleContext(ListstatementsContext.class,0);
		}
		public TerminalNode KEY_ENDFOR() { return getToken(BKITParser.KEY_ENDFOR, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public For_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_statement; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitFor_statement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final For_statementContext for_statement() throws RecognitionException {
		For_statementContext _localctx = new For_statementContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_for_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(228);
			match(KEY_FOR);
			setState(229);
			match(LP);
			setState(230);
			var();
			setState(231);
			match(ASSIGN);
			setState(232);
			exp(0);
			setState(233);
			match(CM);
			setState(234);
			exp(0);
			setState(235);
			match(CM);
			setState(236);
			var();
			setState(237);
			match(ASSIGN);
			setState(238);
			exp(0);
			setState(239);
			match(RP);
			setState(240);
			match(KEY_DO);
			setState(241);
			liststatements();
			setState(242);
			match(KEY_ENDFOR);
			setState(243);
			match(DOT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class While_statementContext extends ParserRuleContext {
		public TerminalNode KEY_WHILE() { return getToken(BKITParser.KEY_WHILE, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode KEY_DO() { return getToken(BKITParser.KEY_DO, 0); }
		public ListstatementsContext liststatements() {
			return getRuleContext(ListstatementsContext.class,0);
		}
		public TerminalNode KEY_ENDWHILE() { return getToken(BKITParser.KEY_ENDWHILE, 0); }
		public TerminalNode DOT() { return getToken(BKITParser.DOT, 0); }
		public While_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_statement; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitWhile_statement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final While_statementContext while_statement() throws RecognitionException {
		While_statementContext _localctx = new While_statementContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_while_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(245);
			match(KEY_WHILE);
			setState(246);
			exp(0);
			setState(247);
			match(KEY_DO);
			setState(248);
			liststatements();
			setState(249);
			match(KEY_ENDWHILE);
			setState(250);
			match(DOT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Do_while_statementContext extends ParserRuleContext {
		public TerminalNode KEY_DO() { return getToken(BKITParser.KEY_DO, 0); }
		public ListstatementsContext liststatements() {
			return getRuleContext(ListstatementsContext.class,0);
		}
		public TerminalNode KEY_WHILE() { return getToken(BKITParser.KEY_WHILE, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode SM() { return getToken(BKITParser.SM, 0); }
		public Do_while_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_do_while_statement; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitDo_while_statement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Do_while_statementContext do_while_statement() throws RecognitionException {
		Do_while_statementContext _localctx = new Do_while_statementContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_do_while_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(252);
			match(KEY_DO);
			setState(253);
			liststatements();
			setState(254);
			match(KEY_WHILE);
			setState(255);
			exp(0);
			setState(256);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Break_statementContext extends ParserRuleContext {
		public TerminalNode KEY_BREAK() { return getToken(BKITParser.KEY_BREAK, 0); }
		public TerminalNode SM() { return getToken(BKITParser.SM, 0); }
		public Break_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_break_statement; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitBreak_statement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Break_statementContext break_statement() throws RecognitionException {
		Break_statementContext _localctx = new Break_statementContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_break_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			match(KEY_BREAK);
			setState(259);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Continue_statementContext extends ParserRuleContext {
		public TerminalNode KEY_CONTINUE() { return getToken(BKITParser.KEY_CONTINUE, 0); }
		public TerminalNode SM() { return getToken(BKITParser.SM, 0); }
		public Continue_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_continue_statement; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitContinue_statement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Continue_statementContext continue_statement() throws RecognitionException {
		Continue_statementContext _localctx = new Continue_statementContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_continue_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(261);
			match(KEY_CONTINUE);
			setState(262);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Call_statementContext extends ParserRuleContext {
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public TerminalNode SM() { return getToken(BKITParser.SM, 0); }
		public Call_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call_statement; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitCall_statement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Call_statementContext call_statement() throws RecognitionException {
		Call_statementContext _localctx = new Call_statementContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_call_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(264);
			func_call();
			setState(265);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Return_statementContext extends ParserRuleContext {
		public TerminalNode KEY_RETURN() { return getToken(BKITParser.KEY_RETURN, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode SM() { return getToken(BKITParser.SM, 0); }
		public Return_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_statement; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitReturn_statement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Return_statementContext return_statement() throws RecognitionException {
		Return_statementContext _localctx = new Return_statementContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_return_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(KEY_RETURN);
			setState(268);
			exp(0);
			setState(269);
			match(SM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpContext extends ParserRuleContext {
		public Exp1Context exp1() {
			return getRuleContext(Exp1Context.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode EQUAL() { return getToken(BKITParser.EQUAL, 0); }
		public TerminalNode NOTEQUAL() { return getToken(BKITParser.NOTEQUAL, 0); }
		public TerminalNode LESS() { return getToken(BKITParser.LESS, 0); }
		public TerminalNode GREATER() { return getToken(BKITParser.GREATER, 0); }
		public TerminalNode LESSEQUAL() { return getToken(BKITParser.LESSEQUAL, 0); }
		public TerminalNode GREATEREQUAL() { return getToken(BKITParser.GREATEREQUAL, 0); }
		public TerminalNode FNOTEQUAL() { return getToken(BKITParser.FNOTEQUAL, 0); }
		public TerminalNode FLESS() { return getToken(BKITParser.FLESS, 0); }
		public TerminalNode FGREATER() { return getToken(BKITParser.FGREATER, 0); }
		public TerminalNode FLESSEQUAL() { return getToken(BKITParser.FLESSEQUAL, 0); }
		public TerminalNode FGREATEREQUAL() { return getToken(BKITParser.FGREATEREQUAL, 0); }
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitExp(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpContext exp() throws RecognitionException {
		return exp(0);
	}

	private ExpContext exp(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpContext _localctx = new ExpContext(_ctx, _parentState);
		ExpContext _prevctx = _localctx;
		int _startState = 58;
		enterRecursionRule(_localctx, 58, RULE_exp, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(272);
			exp1(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(309);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(307);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
					case 1:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(274);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(275);
						match(EQUAL);
						setState(276);
						exp1(0);
						}
						break;
					case 2:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(277);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(278);
						match(NOTEQUAL);
						setState(279);
						exp1(0);
						}
						break;
					case 3:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(280);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(281);
						match(LESS);
						setState(282);
						exp1(0);
						}
						break;
					case 4:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(283);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(284);
						match(GREATER);
						setState(285);
						exp1(0);
						}
						break;
					case 5:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(286);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(287);
						match(LESSEQUAL);
						setState(288);
						exp1(0);
						}
						break;
					case 6:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(289);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(290);
						match(GREATEREQUAL);
						setState(291);
						exp1(0);
						}
						break;
					case 7:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(292);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(293);
						match(FNOTEQUAL);
						setState(294);
						exp1(0);
						}
						break;
					case 8:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(295);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(296);
						match(FLESS);
						setState(297);
						exp1(0);
						}
						break;
					case 9:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(298);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(299);
						match(FGREATER);
						setState(300);
						exp1(0);
						}
						break;
					case 10:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(301);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(302);
						match(FLESSEQUAL);
						setState(303);
						exp1(0);
						}
						break;
					case 11:
						{
						_localctx = new ExpContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp);
						setState(304);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(305);
						match(FGREATEREQUAL);
						setState(306);
						exp1(0);
						}
						break;
					}
					} 
				}
				setState(311);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Exp1Context extends ParserRuleContext {
		public Exp2Context exp2() {
			return getRuleContext(Exp2Context.class,0);
		}
		public Exp1Context exp1() {
			return getRuleContext(Exp1Context.class,0);
		}
		public TerminalNode AND() { return getToken(BKITParser.AND, 0); }
		public TerminalNode OR() { return getToken(BKITParser.OR, 0); }
		public Exp1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp1; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitExp1(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Exp1Context exp1() throws RecognitionException {
		return exp1(0);
	}

	private Exp1Context exp1(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Exp1Context _localctx = new Exp1Context(_ctx, _parentState);
		Exp1Context _prevctx = _localctx;
		int _startState = 60;
		enterRecursionRule(_localctx, 60, RULE_exp1, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(313);
			exp2(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(323);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(321);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
					case 1:
						{
						_localctx = new Exp1Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp1);
						setState(315);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(316);
						match(AND);
						setState(317);
						exp2(0);
						}
						break;
					case 2:
						{
						_localctx = new Exp1Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp1);
						setState(318);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(319);
						match(OR);
						setState(320);
						exp2(0);
						}
						break;
					}
					} 
				}
				setState(325);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Exp2Context extends ParserRuleContext {
		public Exp3Context exp3() {
			return getRuleContext(Exp3Context.class,0);
		}
		public Exp2Context exp2() {
			return getRuleContext(Exp2Context.class,0);
		}
		public TerminalNode ADD() { return getToken(BKITParser.ADD, 0); }
		public TerminalNode FADD() { return getToken(BKITParser.FADD, 0); }
		public TerminalNode SUB() { return getToken(BKITParser.SUB, 0); }
		public TerminalNode FSUB() { return getToken(BKITParser.FSUB, 0); }
		public Exp2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp2; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitExp2(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Exp2Context exp2() throws RecognitionException {
		return exp2(0);
	}

	private Exp2Context exp2(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Exp2Context _localctx = new Exp2Context(_ctx, _parentState);
		Exp2Context _prevctx = _localctx;
		int _startState = 62;
		enterRecursionRule(_localctx, 62, RULE_exp2, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(327);
			exp3(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(343);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(341);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
					case 1:
						{
						_localctx = new Exp2Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp2);
						setState(329);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(330);
						match(ADD);
						setState(331);
						exp3(0);
						}
						break;
					case 2:
						{
						_localctx = new Exp2Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp2);
						setState(332);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(333);
						match(FADD);
						setState(334);
						exp3(0);
						}
						break;
					case 3:
						{
						_localctx = new Exp2Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp2);
						setState(335);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(336);
						match(SUB);
						setState(337);
						exp3(0);
						}
						break;
					case 4:
						{
						_localctx = new Exp2Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp2);
						setState(338);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(339);
						match(FSUB);
						setState(340);
						exp3(0);
						}
						break;
					}
					} 
				}
				setState(345);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,21,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Exp3Context extends ParserRuleContext {
		public Exp4Context exp4() {
			return getRuleContext(Exp4Context.class,0);
		}
		public Exp3Context exp3() {
			return getRuleContext(Exp3Context.class,0);
		}
		public TerminalNode MUL() { return getToken(BKITParser.MUL, 0); }
		public TerminalNode FMUL() { return getToken(BKITParser.FMUL, 0); }
		public TerminalNode DIV() { return getToken(BKITParser.DIV, 0); }
		public TerminalNode FDIV() { return getToken(BKITParser.FDIV, 0); }
		public TerminalNode MOD() { return getToken(BKITParser.MOD, 0); }
		public Exp3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp3; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitExp3(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Exp3Context exp3() throws RecognitionException {
		return exp3(0);
	}

	private Exp3Context exp3(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Exp3Context _localctx = new Exp3Context(_ctx, _parentState);
		Exp3Context _prevctx = _localctx;
		int _startState = 64;
		enterRecursionRule(_localctx, 64, RULE_exp3, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(347);
			exp4();
			}
			_ctx.stop = _input.LT(-1);
			setState(366);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(364);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,22,_ctx) ) {
					case 1:
						{
						_localctx = new Exp3Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp3);
						setState(349);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(350);
						match(MUL);
						setState(351);
						exp4();
						}
						break;
					case 2:
						{
						_localctx = new Exp3Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp3);
						setState(352);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(353);
						match(FMUL);
						setState(354);
						exp4();
						}
						break;
					case 3:
						{
						_localctx = new Exp3Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp3);
						setState(355);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(356);
						match(DIV);
						setState(357);
						exp4();
						}
						break;
					case 4:
						{
						_localctx = new Exp3Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp3);
						setState(358);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(359);
						match(FDIV);
						setState(360);
						exp4();
						}
						break;
					case 5:
						{
						_localctx = new Exp3Context(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_exp3);
						setState(361);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(362);
						match(MOD);
						setState(363);
						exp4();
						}
						break;
					}
					} 
				}
				setState(368);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Exp4Context extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(BKITParser.NOT, 0); }
		public Exp5Context exp5() {
			return getRuleContext(Exp5Context.class,0);
		}
		public Exp4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp4; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitExp4(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Exp4Context exp4() throws RecognitionException {
		Exp4Context _localctx = new Exp4Context(_ctx, getState());
		enterRule(_localctx, 66, RULE_exp4);
		try {
			setState(372);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(369);
				match(NOT);
				setState(370);
				exp5();
				}
				break;
			case SUB:
			case FSUB:
			case LSB:
			case LP:
			case INTLIT:
			case FLOATLIT:
			case BOOLLIT:
			case STRINGLIT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(371);
				exp5();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exp5Context extends ParserRuleContext {
		public TerminalNode SUB() { return getToken(BKITParser.SUB, 0); }
		public Exp6Context exp6() {
			return getRuleContext(Exp6Context.class,0);
		}
		public TerminalNode FSUB() { return getToken(BKITParser.FSUB, 0); }
		public Exp5Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp5; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitExp5(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Exp5Context exp5() throws RecognitionException {
		Exp5Context _localctx = new Exp5Context(_ctx, getState());
		enterRule(_localctx, 68, RULE_exp5);
		try {
			setState(379);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUB:
				enterOuterAlt(_localctx, 1);
				{
				setState(374);
				match(SUB);
				setState(375);
				exp6();
				}
				break;
			case FSUB:
				enterOuterAlt(_localctx, 2);
				{
				setState(376);
				match(FSUB);
				setState(377);
				exp6();
				}
				break;
			case LSB:
			case LP:
			case INTLIT:
			case FLOATLIT:
			case BOOLLIT:
			case STRINGLIT:
			case ID:
				enterOuterAlt(_localctx, 3);
				{
				setState(378);
				exp6();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exp6Context extends ParserRuleContext {
		public TerminalNode LSB() { return getToken(BKITParser.LSB, 0); }
		public Exp7Context exp7() {
			return getRuleContext(Exp7Context.class,0);
		}
		public TerminalNode RSB() { return getToken(BKITParser.RSB, 0); }
		public Exp6Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp6; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitExp6(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Exp6Context exp6() throws RecognitionException {
		Exp6Context _localctx = new Exp6Context(_ctx, getState());
		enterRule(_localctx, 70, RULE_exp6);
		try {
			setState(386);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LSB:
				enterOuterAlt(_localctx, 1);
				{
				setState(381);
				match(LSB);
				setState(382);
				exp7();
				setState(383);
				match(RSB);
				}
				break;
			case LP:
			case INTLIT:
			case FLOATLIT:
			case BOOLLIT:
			case STRINGLIT:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(385);
				exp7();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Exp7Context extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode LP() { return getToken(BKITParser.LP, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode RP() { return getToken(BKITParser.RP, 0); }
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public Element_expContext element_exp() {
			return getRuleContext(Element_expContext.class,0);
		}
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public Exp7Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp7; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitExp7(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Exp7Context exp7() throws RecognitionException {
		Exp7Context _localctx = new Exp7Context(_ctx, getState());
		enterRule(_localctx, 72, RULE_exp7);
		try {
			setState(396);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(388);
				literal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(389);
				match(LP);
				setState(390);
				exp(0);
				setState(391);
				match(RP);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(393);
				match(ID);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(394);
				element_exp();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(395);
				func_call();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Element_expContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public Index_operatorsContext index_operators() {
			return getRuleContext(Index_operatorsContext.class,0);
		}
		public Element_expContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_element_exp; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitElement_exp(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Element_expContext element_exp() throws RecognitionException {
		Element_expContext _localctx = new Element_expContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_element_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(398);
			match(ID);
			setState(399);
			index_operators();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Index_operatorsContext extends ParserRuleContext {
		public TerminalNode LSB() { return getToken(BKITParser.LSB, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode RSB() { return getToken(BKITParser.RSB, 0); }
		public Index_operatorsContext index_operators() {
			return getRuleContext(Index_operatorsContext.class,0);
		}
		public Index_operatorsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_index_operators; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitIndex_operators(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Index_operatorsContext index_operators() throws RecognitionException {
		Index_operatorsContext _localctx = new Index_operatorsContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_index_operators);
		try {
			setState(410);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(401);
				match(LSB);
				setState(402);
				exp(0);
				setState(403);
				match(RSB);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(405);
				match(LSB);
				setState(406);
				exp(0);
				setState(407);
				match(RSB);
				setState(408);
				index_operators();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public TerminalNode LP() { return getToken(BKITParser.LP, 0); }
		public ListExpContext listExp() {
			return getRuleContext(ListExpContext.class,0);
		}
		public TerminalNode RP() { return getToken(BKITParser.RP, 0); }
		public Func_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_call; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitFunc_call(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Func_callContext func_call() throws RecognitionException {
		Func_callContext _localctx = new Func_callContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_func_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(412);
			match(ID);
			setState(413);
			match(LP);
			setState(414);
			listExp();
			setState(415);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ListExpContext extends ParserRuleContext {
		public NoNullListExpContext noNullListExp() {
			return getRuleContext(NoNullListExpContext.class,0);
		}
		public ListExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listExp; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitListExp(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ListExpContext listExp() throws RecognitionException {
		ListExpContext _localctx = new ListExpContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_listExp);
		try {
			setState(419);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUB:
			case FSUB:
			case NOT:
			case LSB:
			case LP:
			case INTLIT:
			case FLOATLIT:
			case BOOLLIT:
			case STRINGLIT:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(417);
				noNullListExp();
				}
				break;
			case RP:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NoNullListExpContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode CM() { return getToken(BKITParser.CM, 0); }
		public NoNullListExpContext noNullListExp() {
			return getRuleContext(NoNullListExpContext.class,0);
		}
		public NoNullListExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_noNullListExp; }
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof BKITVisitor ) return ((BKITVisitor<? extends T>)visitor).visitNoNullListExp(this);
			else return visitor.visitChildren(this);
		}
	}

	public final NoNullListExpContext noNullListExp() throws RecognitionException {
		NoNullListExpContext _localctx = new NoNullListExpContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_noNullListExp);
		try {
			setState(426);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,30,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(421);
				exp(0);
				setState(422);
				match(CM);
				setState(423);
				noNullListExp();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(425);
				exp(0);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 29:
			return exp_sempred((ExpContext)_localctx, predIndex);
		case 30:
			return exp1_sempred((Exp1Context)_localctx, predIndex);
		case 31:
			return exp2_sempred((Exp2Context)_localctx, predIndex);
		case 32:
			return exp3_sempred((Exp3Context)_localctx, predIndex);
		}
		return true;
	}
	private boolean exp_sempred(ExpContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 12);
		case 1:
			return precpred(_ctx, 11);
		case 2:
			return precpred(_ctx, 10);
		case 3:
			return precpred(_ctx, 9);
		case 4:
			return precpred(_ctx, 8);
		case 5:
			return precpred(_ctx, 7);
		case 6:
			return precpred(_ctx, 6);
		case 7:
			return precpred(_ctx, 5);
		case 8:
			return precpred(_ctx, 4);
		case 9:
			return precpred(_ctx, 3);
		case 10:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exp1_sempred(Exp1Context _localctx, int predIndex) {
		switch (predIndex) {
		case 11:
			return precpred(_ctx, 3);
		case 12:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exp2_sempred(Exp2Context _localctx, int predIndex) {
		switch (predIndex) {
		case 13:
			return precpred(_ctx, 5);
		case 14:
			return precpred(_ctx, 4);
		case 15:
			return precpred(_ctx, 3);
		case 16:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean exp3_sempred(Exp3Context _localctx, int predIndex) {
		switch (predIndex) {
		case 17:
			return precpred(_ctx, 6);
		case 18:
			return precpred(_ctx, 5);
		case 19:
			return precpred(_ctx, 4);
		case 20:
			return precpred(_ctx, 3);
		case 21:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A\u01af\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3"+
		"\2\3\2\3\2\3\2\3\3\3\3\5\3]\n\3\3\4\3\4\5\4a\n\4\3\5\3\5\3\5\3\5\5\5g"+
		"\n\5\3\6\3\6\3\6\3\6\5\6m\n\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b"+
		"\5\by\n\b\3\t\3\t\5\t}\n\t\3\n\3\n\5\n\u0081\n\n\3\13\3\13\3\13\3\13\3"+
		"\13\3\13\3\13\5\13\u008a\n\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r"+
		"\5\r\u0096\n\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17"+
		"\3\17\3\17\3\17\5\17\u00a6\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00ad\n"+
		"\20\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\5\23\u00b9\n\23"+
		"\3\24\3\24\3\24\3\24\5\24\u00bf\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25"+
		"\3\25\3\25\3\25\5\25\u00cb\n\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u00db\n\27\f\27\16\27\u00de\13\27"+
		"\3\27\3\27\5\27\u00e2\n\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30"+
		"\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34"+
		"\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37"+
		"\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37"+
		"\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37"+
		"\3\37\3\37\3\37\7\37\u0136\n\37\f\37\16\37\u0139\13\37\3 \3 \3 \3 \3 "+
		"\3 \3 \3 \3 \7 \u0144\n \f \16 \u0147\13 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3"+
		"!\3!\3!\3!\3!\3!\7!\u0158\n!\f!\16!\u015b\13!\3\"\3\"\3\"\3\"\3\"\3\""+
		"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\7\"\u016f\n\"\f\"\16"+
		"\"\u0172\13\"\3#\3#\3#\5#\u0177\n#\3$\3$\3$\3$\3$\5$\u017e\n$\3%\3%\3"+
		"%\3%\3%\5%\u0185\n%\3&\3&\3&\3&\3&\3&\3&\3&\5&\u018f\n&\3\'\3\'\3\'\3"+
		"(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u019d\n(\3)\3)\3)\3)\3)\3*\3*\5*\u01a6\n"+
		"*\3+\3+\3+\3+\3+\5+\u01ad\n+\3+\2\6<>@B,\2\4\6\b\n\f\16\20\22\24\26\30"+
		"\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRT\2\3\4\2\65\659;\2\u01bd"+
		"\2V\3\2\2\2\4\\\3\2\2\2\6`\3\2\2\2\bf\3\2\2\2\nl\3\2\2\2\fn\3\2\2\2\16"+
		"x\3\2\2\2\20|\3\2\2\2\22\u0080\3\2\2\2\24\u0089\3\2\2\2\26\u008b\3\2\2"+
		"\2\30\u0095\3\2\2\2\32\u0097\3\2\2\2\34\u00a5\3\2\2\2\36\u00ac\3\2\2\2"+
		" \u00ae\3\2\2\2\"\u00b0\3\2\2\2$\u00b8\3\2\2\2&\u00be\3\2\2\2(\u00ca\3"+
		"\2\2\2*\u00cc\3\2\2\2,\u00d1\3\2\2\2.\u00e6\3\2\2\2\60\u00f7\3\2\2\2\62"+
		"\u00fe\3\2\2\2\64\u0104\3\2\2\2\66\u0107\3\2\2\28\u010a\3\2\2\2:\u010d"+
		"\3\2\2\2<\u0111\3\2\2\2>\u013a\3\2\2\2@\u0148\3\2\2\2B\u015c\3\2\2\2D"+
		"\u0176\3\2\2\2F\u017d\3\2\2\2H\u0184\3\2\2\2J\u018e\3\2\2\2L\u0190\3\2"+
		"\2\2N\u019c\3\2\2\2P\u019e\3\2\2\2R\u01a5\3\2\2\2T\u01ac\3\2\2\2VW\5\4"+
		"\3\2WX\5\6\4\2XY\7\2\2\3Y\3\3\2\2\2Z]\5\b\5\2[]\3\2\2\2\\Z\3\2\2\2\\["+
		"\3\2\2\2]\5\3\2\2\2^a\5\n\6\2_a\3\2\2\2`^\3\2\2\2`_\3\2\2\2a\7\3\2\2\2"+
		"bc\5\f\7\2cd\5\b\5\2dg\3\2\2\2eg\5\f\7\2fb\3\2\2\2fe\3\2\2\2g\t\3\2\2"+
		"\2hi\5\34\17\2ij\5\n\6\2jm\3\2\2\2km\5\34\17\2lh\3\2\2\2lk\3\2\2\2m\13"+
		"\3\2\2\2no\7*\2\2op\7\60\2\2pq\5\16\b\2qr\7\63\2\2r\r\3\2\2\2st\5\20\t"+
		"\2tu\7\62\2\2uv\5\16\b\2vy\3\2\2\2wy\5\20\t\2xs\3\2\2\2xw\3\2\2\2y\17"+
		"\3\2\2\2z}\5\22\n\2{}\5\24\13\2|z\3\2\2\2|{\3\2\2\2}\21\3\2\2\2~\u0081"+
		"\7<\2\2\177\u0081\5\26\f\2\u0080~\3\2\2\2\u0080\177\3\2\2\2\u0081\23\3"+
		"\2\2\2\u0082\u0083\7<\2\2\u0083\u0084\7\64\2\2\u0084\u008a\5\32\16\2\u0085"+
		"\u0086\5\26\f\2\u0086\u0087\7\64\2\2\u0087\u0088\5\32\16\2\u0088\u008a"+
		"\3\2\2\2\u0089\u0082\3\2\2\2\u0089\u0085\3\2\2\2\u008a\25\3\2\2\2\u008b"+
		"\u008c\7<\2\2\u008c\u008d\5\30\r\2\u008d\27\3\2\2\2\u008e\u008f\7,\2\2"+
		"\u008f\u0090\7\65\2\2\u0090\u0096\7-\2\2\u0091\u0092\7,\2\2\u0092\u0093"+
		"\7\65\2\2\u0093\u0094\7-\2\2\u0094\u0096\5\30\r\2\u0095\u008e\3\2\2\2"+
		"\u0095\u0091\3\2\2\2\u0096\31\3\2\2\2\u0097\u0098\t\2\2\2\u0098\33\3\2"+
		"\2\2\u0099\u009a\7%\2\2\u009a\u009b\7\60\2\2\u009b\u009c\7<\2\2\u009c"+
		"\u009d\7\'\2\2\u009d\u009e\7\60\2\2\u009e\u009f\5\36\20\2\u009f\u00a0"+
		"\5\"\22\2\u00a0\u00a6\3\2\2\2\u00a1\u00a2\7%\2\2\u00a2\u00a3\7\60\2\2"+
		"\u00a3\u00a4\7<\2\2\u00a4\u00a6\5\"\22\2\u00a5\u0099\3\2\2\2\u00a5\u00a1"+
		"\3\2\2\2\u00a6\35\3\2\2\2\u00a7\u00a8\5 \21\2\u00a8\u00a9\7\62\2\2\u00a9"+
		"\u00aa\5\36\20\2\u00aa\u00ad\3\2\2\2\u00ab\u00ad\5 \21\2\u00ac\u00a7\3"+
		"\2\2\2\u00ac\u00ab\3\2\2\2\u00ad\37\3\2\2\2\u00ae\u00af\7<\2\2\u00af!"+
		"\3\2\2\2\u00b0\u00b1\7\32\2\2\u00b1\u00b2\7\60\2\2\u00b2\u00b3\5$\23\2"+
		"\u00b3\u00b4\7 \2\2\u00b4\u00b5\7\61\2\2\u00b5#\3\2\2\2\u00b6\u00b9\5"+
		"&\24\2\u00b7\u00b9\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9"+
		"%\3\2\2\2\u00ba\u00bb\5(\25\2\u00bb\u00bc\5&\24\2\u00bc\u00bf\3\2\2\2"+
		"\u00bd\u00bf\5(\25\2\u00be\u00ba\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf\'\3"+
		"\2\2\2\u00c0\u00cb\5\f\7\2\u00c1\u00cb\5*\26\2\u00c2\u00cb\5,\27\2\u00c3"+
		"\u00cb\5.\30\2\u00c4\u00cb\5\60\31\2\u00c5\u00cb\5\62\32\2\u00c6\u00cb"+
		"\5\64\33\2\u00c7\u00cb\5\66\34\2\u00c8\u00cb\58\35\2\u00c9\u00cb\5:\36"+
		"\2\u00ca\u00c0\3\2\2\2\u00ca\u00c1\3\2\2\2\u00ca\u00c2\3\2\2\2\u00ca\u00c3"+
		"\3\2\2\2\u00ca\u00c4\3\2\2\2\u00ca\u00c5\3\2\2\2\u00ca\u00c6\3\2\2\2\u00ca"+
		"\u00c7\3\2\2\2\u00ca\u00c8\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb)\3\2\2\2"+
		"\u00cc\u00cd\5\20\t\2\u00cd\u00ce\7\64\2\2\u00ce\u00cf\5<\37\2\u00cf\u00d0"+
		"\7\63\2\2\u00d0+\3\2\2\2\u00d1\u00d2\7&\2\2\u00d2\u00d3\5<\37\2\u00d3"+
		"\u00d4\7)\2\2\u00d4\u00dc\5$\23\2\u00d5\u00d6\7\37\2\2\u00d6\u00d7\5<"+
		"\37\2\u00d7\u00d8\7)\2\2\u00d8\u00d9\5$\23\2\u00d9\u00db\3\2\2\2\u00da"+
		"\u00d5\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2"+
		"\2\2\u00dd\u00e1\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e0\7\36\2\2\u00e0"+
		"\u00e2\5$\23\2\u00e1\u00df\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3\3\2"+
		"\2\2\u00e3\u00e4\7!\2\2\u00e4\u00e5\7\61\2\2\u00e5-\3\2\2\2\u00e6\u00e7"+
		"\7$\2\2\u00e7\u00e8\7.\2\2\u00e8\u00e9\5\20\t\2\u00e9\u00ea\7\64\2\2\u00ea"+
		"\u00eb\5<\37\2\u00eb\u00ec\7\62\2\2\u00ec\u00ed\5<\37\2\u00ed\u00ee\7"+
		"\62\2\2\u00ee\u00ef\5\20\t\2\u00ef\u00f0\7\64\2\2\u00f0\u00f1\5<\37\2"+
		"\u00f1\u00f2\7/\2\2\u00f2\u00f3\7\35\2\2\u00f3\u00f4\5$\23\2\u00f4\u00f5"+
		"\7\"\2\2\u00f5\u00f6\7\61\2\2\u00f6/\3\2\2\2\u00f7\u00f8\7+\2\2\u00f8"+
		"\u00f9\5<\37\2\u00f9\u00fa\7\35\2\2\u00fa\u00fb\5$\23\2\u00fb\u00fc\7"+
		"#\2\2\u00fc\u00fd\7\61\2\2\u00fd\61\3\2\2\2\u00fe\u00ff\7\35\2\2\u00ff"+
		"\u0100\5$\23\2\u0100\u0101\7+\2\2\u0101\u0102\5<\37\2\u0102\u0103\7\63"+
		"\2\2\u0103\63\3\2\2\2\u0104\u0105\7\33\2\2\u0105\u0106\7\63\2\2\u0106"+
		"\65\3\2\2\2\u0107\u0108\7\34\2\2\u0108\u0109\7\63\2\2\u0109\67\3\2\2\2"+
		"\u010a\u010b\5P)\2\u010b\u010c\7\63\2\2\u010c9\3\2\2\2\u010d\u010e\7("+
		"\2\2\u010e\u010f\5<\37\2\u010f\u0110\7\63\2\2\u0110;\3\2\2\2\u0111\u0112"+
		"\b\37\1\2\u0112\u0113\5> \2\u0113\u0137\3\2\2\2\u0114\u0115\f\16\2\2\u0115"+
		"\u0116\7\17\2\2\u0116\u0136\5> \2\u0117\u0118\f\r\2\2\u0118\u0119\7\20"+
		"\2\2\u0119\u0136\5> \2\u011a\u011b\f\f\2\2\u011b\u011c\7\21\2\2\u011c"+
		"\u0136\5> \2\u011d\u011e\f\13\2\2\u011e\u011f\7\22\2\2\u011f\u0136\5>"+
		" \2\u0120\u0121\f\n\2\2\u0121\u0122\7\23\2\2\u0122\u0136\5> \2\u0123\u0124"+
		"\f\t\2\2\u0124\u0125\7\24\2\2\u0125\u0136\5> \2\u0126\u0127\f\b\2\2\u0127"+
		"\u0128\7\25\2\2\u0128\u0136\5> \2\u0129\u012a\f\7\2\2\u012a\u012b\7\26"+
		"\2\2\u012b\u0136\5> \2\u012c\u012d\f\6\2\2\u012d\u012e\7\27\2\2\u012e"+
		"\u0136\5> \2\u012f\u0130\f\5\2\2\u0130\u0131\7\30\2\2\u0131\u0136\5> "+
		"\2\u0132\u0133\f\4\2\2\u0133\u0134\7\31\2\2\u0134\u0136\5> \2\u0135\u0114"+
		"\3\2\2\2\u0135\u0117\3\2\2\2\u0135\u011a\3\2\2\2\u0135\u011d\3\2\2\2\u0135"+
		"\u0120\3\2\2\2\u0135\u0123\3\2\2\2\u0135\u0126\3\2\2\2\u0135\u0129\3\2"+
		"\2\2\u0135\u012c\3\2\2\2\u0135\u012f\3\2\2\2\u0135\u0132\3\2\2\2\u0136"+
		"\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138=\3\2\2\2"+
		"\u0139\u0137\3\2\2\2\u013a\u013b\b \1\2\u013b\u013c\5@!\2\u013c\u0145"+
		"\3\2\2\2\u013d\u013e\f\5\2\2\u013e\u013f\7\r\2\2\u013f\u0144\5@!\2\u0140"+
		"\u0141\f\4\2\2\u0141\u0142\7\16\2\2\u0142\u0144\5@!\2\u0143\u013d\3\2"+
		"\2\2\u0143\u0140\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0143\3\2\2\2\u0145"+
		"\u0146\3\2\2\2\u0146?\3\2\2\2\u0147\u0145\3\2\2\2\u0148\u0149\b!\1\2\u0149"+
		"\u014a\5B\"\2\u014a\u0159\3\2\2\2\u014b\u014c\f\7\2\2\u014c\u014d\7\3"+
		"\2\2\u014d\u0158\5B\"\2\u014e\u014f\f\6\2\2\u014f\u0150\7\4\2\2\u0150"+
		"\u0158\5B\"\2\u0151\u0152\f\5\2\2\u0152\u0153\7\5\2\2\u0153\u0158\5B\""+
		"\2\u0154\u0155\f\4\2\2\u0155\u0156\7\6\2\2\u0156\u0158\5B\"\2\u0157\u014b"+
		"\3\2\2\2\u0157\u014e\3\2\2\2\u0157\u0151\3\2\2\2\u0157\u0154\3\2\2\2\u0158"+
		"\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015aA\3\2\2\2"+
		"\u015b\u0159\3\2\2\2\u015c\u015d\b\"\1\2\u015d\u015e\5D#\2\u015e\u0170"+
		"\3\2\2\2\u015f\u0160\f\b\2\2\u0160\u0161\7\7\2\2\u0161\u016f\5D#\2\u0162"+
		"\u0163\f\7\2\2\u0163\u0164\7\b\2\2\u0164\u016f\5D#\2\u0165\u0166\f\6\2"+
		"\2\u0166\u0167\7\t\2\2\u0167\u016f\5D#\2\u0168\u0169\f\5\2\2\u0169\u016a"+
		"\7\n\2\2\u016a\u016f\5D#\2\u016b\u016c\f\4\2\2\u016c\u016d\7\13\2\2\u016d"+
		"\u016f\5D#\2\u016e\u015f\3\2\2\2\u016e\u0162\3\2\2\2\u016e\u0165\3\2\2"+
		"\2\u016e\u0168\3\2\2\2\u016e\u016b\3\2\2\2\u016f\u0172\3\2\2\2\u0170\u016e"+
		"\3\2\2\2\u0170\u0171\3\2\2\2\u0171C\3\2\2\2\u0172\u0170\3\2\2\2\u0173"+
		"\u0174\7\f\2\2\u0174\u0177\5F$\2\u0175\u0177\5F$\2\u0176\u0173\3\2\2\2"+
		"\u0176\u0175\3\2\2\2\u0177E\3\2\2\2\u0178\u0179\7\5\2\2\u0179\u017e\5"+
		"H%\2\u017a\u017b\7\6\2\2\u017b\u017e\5H%\2\u017c\u017e\5H%\2\u017d\u0178"+
		"\3\2\2\2\u017d\u017a\3\2\2\2\u017d\u017c\3\2\2\2\u017eG\3\2\2\2\u017f"+
		"\u0180\7,\2\2\u0180\u0181\5J&\2\u0181\u0182\7-\2\2\u0182\u0185\3\2\2\2"+
		"\u0183\u0185\5J&\2\u0184\u017f\3\2\2\2\u0184\u0183\3\2\2\2\u0185I\3\2"+
		"\2\2\u0186\u018f\5\32\16\2\u0187\u0188\7.\2\2\u0188\u0189\5<\37\2\u0189"+
		"\u018a\7/\2\2\u018a\u018f\3\2\2\2\u018b\u018f\7<\2\2\u018c\u018f\5L\'"+
		"\2\u018d\u018f\5P)\2\u018e\u0186\3\2\2\2\u018e\u0187\3\2\2\2\u018e\u018b"+
		"\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018d\3\2\2\2\u018fK\3\2\2\2\u0190"+
		"\u0191\7<\2\2\u0191\u0192\5N(\2\u0192M\3\2\2\2\u0193\u0194\7,\2\2\u0194"+
		"\u0195\5<\37\2\u0195\u0196\7-\2\2\u0196\u019d\3\2\2\2\u0197\u0198\7,\2"+
		"\2\u0198\u0199\5<\37\2\u0199\u019a\7-\2\2\u019a\u019b\5N(\2\u019b\u019d"+
		"\3\2\2\2\u019c\u0193\3\2\2\2\u019c\u0197\3\2\2\2\u019dO\3\2\2\2\u019e"+
		"\u019f\7<\2\2\u019f\u01a0\7.\2\2\u01a0\u01a1\5R*\2\u01a1\u01a2\7/\2\2"+
		"\u01a2Q\3\2\2\2\u01a3\u01a6\5T+\2\u01a4\u01a6\3\2\2\2\u01a5\u01a3\3\2"+
		"\2\2\u01a5\u01a4\3\2\2\2\u01a6S\3\2\2\2\u01a7\u01a8\5<\37\2\u01a8\u01a9"+
		"\7\62\2\2\u01a9\u01aa\5T+\2\u01aa\u01ad\3\2\2\2\u01ab\u01ad\5<\37\2\u01ac"+
		"\u01a7\3\2\2\2\u01ac\u01ab\3\2\2\2\u01adU\3\2\2\2!\\`flx|\u0080\u0089"+
		"\u0095\u00a5\u00ac\u00b8\u00be\u00ca\u00dc\u00e1\u0135\u0137\u0143\u0145"+
		"\u0157\u0159\u016e\u0170\u0176\u017d\u0184\u018e\u019c\u01a5\u01ac";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}