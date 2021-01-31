//-----------------
// 1927021 Nguyễn Tuấn Kiệt -----------------
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options {
	language = Python3;
}

program: varDecList? funcDecList? EOF;

// ------------variable declaration-------------------------------

varDecList: varDec varDecList | varDec;

varDec: VAR CL varList SM;

varList: (varLit | varArray) CM varList | (varLit | varArray);

varLit: ID ASSIGN (INTLIT | FLOATLIT | BOOLLIT | STRING) | ID;

varArray: ID varArrayIndex ASSIGN array | ID varArrayIndex;

varArrayIndex: LSB INTLIT RSB | LSB INTLIT RSB varArrayIndex;

// ------------Function declaration-------------------------------
funcDecList: funcDec funcDecList | funcDec;

funcDec: FUNCTION CL ID paramSection bodySection;

paramSection: PARAMETER CL paramList |;

paramList: param | param CM paramList;

param: ID | ID varArrayIndex;

bodySection: BODY CL varDecWithStatementList ENDBODY DOT;

varDecWithStatementList: varDecList? nullableStatementList;

nullableStatementList: statementList |;

statementList: oneStatement | oneStatement statementList;

oneStatement:
	assignStatement
	| ifStatement
	| forStatement
	| whileStatement
	| dowhileStatement
	| breakStatement
	| continueStatement
	| callStatement
	| returnStatement;

variable: ID | arrayElement;

assignStatement: variable ASSIGN expression SM;

ifStatement:
	IF expression THEN varDecWithStatementList (
		ELSEIF expression THEN varDecWithStatementList
	)* (ELSE varDecWithStatementList)? ENDIF DOT;

forStatement:
	FOR LP ID ASSIGN expression CM expression CM expression RP DO varDecWithStatementList ENDFOR DOT
		;

whileStatement:
	WHILE expression DO varDecWithStatementList ENDWHILE DOT;

dowhileStatement:
	DO varDecWithStatementList WHILE expression ENDDO DOT;

breakStatement: BREAK SM;

continueStatement: CONTINUE SM;

callStatement: funcCall SM;

returnStatement: RETURN expression SM | RETURN SM;

relational:
	EQUAL
	| NEQUAL
	| LT
	| GT
	| LTE
	| GTE
	| NEQF
	| GTF
	| LTF
	| GTEF
	| LTEF;

expression: exp1 relational exp1 | exp1;
exp1: exp1 (CONJ | DISJ) exp2 | exp2;
exp2: exp2 (ADD | ADDF | SUB | SUBF) exp3 | exp3;
exp3: exp3 (MUL | MULF | DIV | DIVF | MOD) exp4 | exp4;
exp4: (NOT) exp4 | exp5;
exp5: (SUB | SUBF) exp5 | exp6;
exp6: exp6 indexOperators | exp7;
exp7: funcCall | ID | LP expression RP | literal ;

arrayElement: exp6;

indexOperators:
	LSB expression RSB indexOperators|
	LSB expression RSB;

funcCall: ID LP expList RP | ID LP RP;

expList: expression CM expList | expression;

literal: INTLIT | FLOATLIT | BOOLLIT | STRING | array;

//array
array: LCB INTLIT (CM INTLIT)* RCB
		|	LCB FLOATLIT (CM FLOATLIT)* RCB
		|	LCB BOOLLIT (CM BOOLLIT)* RCB
		|	LCB STRING (CM STRING)* RCB
		|	LCB array (CM array)* RCB;

// LITERALS float
fragment EXPONENT: [eE][+-]? NUMBER+;

FLOATLIT:
	NUMBER+ (DOT NUMBER* | EXPONENT+ | DOT NUMBER* EXPONENT*);

//int
INTLIT: HEX | OCTAL | DEC;

fragment HEX: '0' [xX]([1-9A-F]( NUMBER | [A-F])*);

fragment OCTAL: '0' [oO]( [1-7][0-7]*);

fragment DEC: '0' | [1-9]NUMBER*;

//bool
BOOLLIT: TRUE | FALSE;

//string
fragment ESC_SEQ: '\\' [btnfr'\\];

// fragment ESC_SEQUENCE: BACKSPACE | FORMFEED | CARRIAGE_RETURN | NEWLINE | HORIZONTAL_TAB |
// SINGLE_QUOTE | DOUBLE_QUOTE | BACK_SLASH;

STRING:
	DOUBLE_QUOTE (STR_CHAR)*? DOUBLE_QUOTE {
	self.text = self.text[1:-1]
};

// OPERATOR

ADDF: '+.';

ADD: '+';

SUB: '-';

SUBF: '-.';

MUL: '*';

MULF: '*.';

DIV: '\\';

DIVF: '\\.';

MOD: '%';

// BOOLEAN OPERATORS

NOT: '!';

CONJ: '&&';

DISJ: '||';

// RELATION OPERATORS

EQUAL: '==';

NEQUAL: '!=';

LT: '<';

GT: '>';

LTE: '<=';

GTE: '>=';

NEQF: '=/=';

LTF: '<.';

GTF: '>.';

LTEF: '<=.';

GTEF: '>=.';

//Separators

LSB: '[';

RSB: ']';

LP: '(';

RP: ')';

CL: ':';

DOT: '.';

CM: ',';

SM: ';';

LCB: '{';

RCB: '}';

ASSIGN: '=';

fragment SPACE: [ ]*;
fragment NUMBER: [0-9];
fragment LOWER: [a-z];
fragment UPPER: [A-Z];
fragment UNDERSCORE: '_';

fragment BACKSPACE: '\\b';
fragment FORMFEED: '\\f';
fragment CARRIAGE_RETURN: '\\r';
fragment NEWLINE: '\\n';
fragment HORIZONTAL_TAB: '\\t';
fragment SINGLE_QUOTE: ['];
fragment DOUBLE_QUOTE: ["];
fragment BACK_SLASH: '\\\\"';

// KEYWORD

BODY: 'Body';

BREAK: 'Break';

CONTINUE: 'Continue';

DO: 'Do';

ELSE: 'Else';

ELSEIF: 'ElseIf';

ENDBODY: 'EndBody';

ENDIF: 'EndIf';

ENDFOR: 'EndFor';

ENDWHILE: 'EndWhile';

FOR: 'For';

FUNCTION: 'Function';

IF: 'If';

PARAMETER: 'Parameter';

RETURN: 'Return';

THEN: 'Then';

VAR: 'Var';

WHILE: 'While';

TRUE: 'True';

FALSE: 'False';

ENDDO: 'EndDo';

// ID
ID: LOWER ( LOWER | UPPER | UNDERSCORE | NUMBER)*;

// --------------------------
COMMENT: ('**' COMMENT_CHAR*? '**') -> skip;

WS: [ \t\r\n]+ -> skip;
// skip spaces, tabs, newlines

fragment STR_CHAR: ~[\n\b"'\\] | ESC_SEQ | ('\'' '"');
fragment ESC_ILLEGAL: '\\' ~[btnfr'\\] | '\\' | [']~["];
fragment COMMENT_CHAR: ~[*]| [*]~[*]| [*] EOF;

ERROR_CHAR: .;
UNCLOSE_STRING:
	'"' STR_CHAR* ([\n\r] | EOF) { 
		y = str(self.text) 
		possible = ['\n', '\r'] 
		if y[-1] in possible:
			raise UncloseString(y[1:-1]) 
		else: 
			raise UncloseString(y[1:]) 
	};
ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL { 
		y = str(self.text) 
		raise IllegalEscape(y[1:]) 
	};
UNTERMINATED_COMMENT:
	'**' COMMENT_CHAR* EOF { raise UnterminatedComment() };
