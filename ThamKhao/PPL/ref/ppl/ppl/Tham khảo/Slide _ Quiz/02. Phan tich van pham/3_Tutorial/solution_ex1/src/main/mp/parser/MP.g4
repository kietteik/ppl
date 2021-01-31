grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
//............PARSER: BNF....
program
	: many_decl
	;
many_decl
	: decl many_decl
	| decl
	;
decl
	: var_decl
	| func_decl
	;
var_decl
	: id_type list_id SM
	;
list_id
	: ID CM list_id
	| ID
	;
id_type
	: INT
	| FLOAT
	;
func_decl
	: id_type ID para_decl body
	;

para_decl
	: LP para_list RP
	;
para_list
	: para many_para
	| 
	;
many_para
	: CM para many_para
	| 
	;
para
	:id_type list_id
	;

body
	: LB members RB
	;
members
	: member members
	| 
	;
member	
	: stmt
	| var_decl
	;
stmt
	: ass_stmt
	| call_stmt
	| return_stmt
	;
ass_stmt
	: ID EQ exp SM
	;
call_stmt
	: ID LP list_exp RP SM
	;

return_stmt
	: RETURN exp SM
	;

list_exp
	: exp many_exp
	|
	;
many_exp
	: CM exp many_exp
	|
	;

exp
	: exp1 ADD exp
	| exp1
	;
exp1
	: exp2 SUB exp2
	| exp2
	;
exp2
	: exp2 MUL exp3
	| exp2 DIV exp3
	| exp3
	;
exp3
	: INTLIT
	| FLOATLIT
	| ID 
	| call_stmt
	| LP exp RP
	;
//................LEXER..............
ID: [a-z] [0-9a-z]*;
INTLIT: [0-9]+;
FLOATLIT: [0-9]+ ('.')? [0-9]* [eE]? ('-')? [0-9]+;
INT: 'int' ;
FLOAT: 'float'  ;
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
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines





