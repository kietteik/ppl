// StudentID 1710169
//Nguyen Van Hoai Linh
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit();
        raise UncloseString(result.text[1:])
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        if tk == self.STRINGLIT:
            st = self.text[1:-1]
            self.text = st
        return super().emit();
}
options{
	language=Python3;
}


program: (var_decl | func_decl)+ EOF;

// not support variable initialization, size array must be known

func_decl: func_type func_name LP (one_para (CM one_para)*)? RP block_statement;
func_type: primitive_type | array_output | VOIDTYPE;
func_name: ID;
one_para: primitive_type ID | array_input;
block_statement:LB (var_decl | statement)* RB;

var_decl: primitive_type (one_variable (CM one_variable)* ) SEMI;
one_variable: ID | ID LS INTLIT RS ;

expression_stm:    term1 ASSIGN expression_stm  | term1;
term1:                           term1 OR term2 | term2;
term2:                          term2 AND term3 | term3;
term3:                   term4 (EQ | NEQ) term4 | term4;
term4:term5 (LESS| ELESS | GREAT | EGREAT)term5 | term5;
term5:                  term5 (ADD | SUB) term6 | term6;
term6:            term6 (DIV | MUL | MOD) term7 | term7;
term7:                        (SUB | NOT) term7 | term8;
term8:            term9 ( LS expression_stm RS) | term9;
term9:          (LP expression_stm RP) | operand;
operand: BOOLLIT|FLOATLIT|INTLIT|STRINGLIT|ID|invocation;
//array_element:   LS expression_stm RS;
invocation: ID LP (expression_stm (CM expression_stm)*)? RP;
array_input: primitive_type ID LS RS ;
array_output: primitive_type LS RS;
statement:  if_stm
            |do_while_stm SEMI
            |for_stm
            |break_stm SEMI 
            |continue_stm SEMI
            |return_stm SEMI
            |expression_stm SEMI
            |block_statement;
if_stm:     'if' LP expression_stm RP statement
            |'if' LP expression_stm RP statement 'else' statement;
do_while_stm: 'do' (statement)+ 'while' expression_stm;
for_stm: 'for' LP expression_stm SEMI expression_stm SEMI expression_stm RP statement;
break_stm:'break' ;
continue_stm: 'continue' ;
return_stm: 'return' | 'return' expression_stm;
INTTYPE: 'int' ;

primitive_type: INTTYPE|BOOLTYPE|FLOATTYPE|STRINGTYPE;
func_call:;
VOIDTYPE: 'void';
BOOLTYPE: 'boolean';
FLOATTYPE: 'float';
STRINGTYPE:'string';
//Operator
ADD: '+'; 
MUL: '*';
NOT:'!';
OR:'||';
NEQ:'!=';
LESS:'<';
ELESS:'<=';
ASSIGN:'=';
SUB:'-';
DIV: '/';
MOD:'%';
AND:'&&';
EQ:'==';
GREAT:'>';
EGREAT:'>=';

//Separators
LS: '[';
RS: ']';
LB: '{' ;
RB: '}' ;
LP: '(';
RP: ')';
SEMI:';';
CM:',';

//Literals
BOOLLIT: 'true'|'false';
fragment NUMBER: [0-9];
fragment POINT : '.'; 
fragment EXP: ('e'|'E'|'e-'|'E-');
fragment NOEXP : NUMBER+ POINT NUMBER*| NUMBER* POINT NUMBER+ ;
fragment NOPOINT: NUMBER+ EXP NUMBER+;
fragment ALL: NUMBER* POINT NUMBER+ EXP NUMBER+ | NUMBER+ POINT NUMBER* EXP NUMBER+;
FLOATLIT: NOEXP| NOPOINT | ALL ;
INTLIT:  NUMBER+;
fragment QUOTE: '"';
fragment ESCAPE_SEQUENCE: '\\'[bfrnt"\\];
//fragment ESCAPE_SEQUENCE: [\u0008-\u0013];
fragment ESCAPE_ILLEGAL: '\\'~[bfrnt"\\\n\r];

fragment NOTQUOTE: (~'"');

//STRINGLIT: '"'('\\' [bfrnt"\\] | ~[\r\n"\\EOF])*'"' ;
ID: [_a-zA-Z][_0-9a-zA-Z]* ; 
WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

fragment LCOMMENT: '/*';
fragment RCOMMENT: '*/';
fragment COMMENT: '//';

BLOCKCOMMENT: (  LCOMMENT .*? RCOMMENT )-> skip;
LINECOMMENT: COMMENT (~[\r\n])*         -> skip;
//STRINGLIT:QUOTE(ESCAPE_SEQUENCE | ~[\r\n"\\])*QUOTE;
fragment STRING: (ESCAPE_SEQUENCE| [\u0000-\u0009\u000B\u000C\u000E-\u0021\u0023-\u005B\u005D-\u00FF]);
STRINGLIT:QUOTE STRING*QUOTE;

UNCLOSE_STRING: QUOTE(ESCAPE_SEQUENCE | STRING | '\\' EOF )*| QUOTE'\\';
//ILLEGAL_ESCAPE :QUOTE (ESCAPE_ILLEGAL| STRING)*;
ILLEGAL_ESCAPE :QUOTE STRING* ESCAPE_ILLEGAL;
//44 26 24 53 100 97 86 75 74 26 24 53 97 8
ERROR_CHAR: .;