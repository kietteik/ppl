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

program: (var_dec | func_dec)+ EOF;

var_dec: one_param SM;
func_dec: type_stmt ID LP param_list? RP LB func_body RB;

one_param: type_stmt ( ID (CM ID)*);
param_list: one_param (SM one_param)*;
// param_list1: one_param SM param_list | one_param;
func_body: ( var_dec | stmt)*;
stmt: ( assignment | call | return_stmt) SM;
assignment: ID EQ exp;
call: ID LP (exp (CM exp)*)? RP;
return_stmt: RETURN exp;
exp:
	LB exp RB
	| exp MUL exp
	| exp DIV exp
	| exp SUB exp
	| <assoc = right> exp ADD exp
	| INTLIT
	| FLOATLIT
	| ID
	| call;

type_stmt: INT | FLOAT;

fragment LETTER: [a-z];
fragment NUMBER: [0-9];
fragment DOT: '.';

ID: LETTER (LETTER | NUMBER)*;
INTLIT: NUMBER+;
FLOATLIT:
	NUMBER+ ((DOT NUMBER+ [eE][+-]?) | (DOT | ([eE][+-]?))) NUMBER+;
INT: 'int';
FLOAT: 'float';
RETURN: 'return';

LB: '{';
RB: '}';
SM: ';';
CM: ',';
EQ: '=';
LP: '(';
RP: ')';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

COLON: ':';
VAR: 'Var';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;