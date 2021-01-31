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

options{
	language=Python3;
}

program: (variable_declaration | function_declaration)* ;

variable_declaration: data_type ID (CM ID)* SM;
function_declaration: data_type ID parameter_declaration function_body;
function_body: LB (variable_declaration | statement)* RB;
parameter_declaration: LP parameter_list? RP;
variable_parameter: data_type ID (CM ID)*;
parameter_list: variable_parameter (SM variable_parameter)*;


expression: exp1 ADD expression | exp1;
exp1: exp1 SUB exp2 | exp2;
exp2: exp2 (MUL | DIV) exp3 | exp3;
exp3: LP expression RP | operands;

operands: INTLIT | FLOATLIT | ID | call_function; 

statement: assignment | call_statement | return_statement;
in_parameters: expression (CM expression)*;
call_function: ID LP in_parameters? RP;
call_statement: call_function SM;
assignment: ID EQ expression SM;
return_statement: RETURN expression SM;

data_type: INT | FLOAT;

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
ID: ('_' | ALPHA) ('_'| ALPHA | DIGIT)*;
INTLIT: [1-9] DIGIT* | '0'+;
FLOATLIT: INT_PART (DEC_PART EXP_PART | DEC_PART | EXP_PART);
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;

fragment ALPHA: [a-zA-Z];
fragment DIGIT: [0-9];
fragment INT_PART: [1-9] DIGIT* | '0'+;
fragment DEC_PART: '.' DIGIT+;
fragment EXP_PART: [eE] '-'? DIGIT+;
