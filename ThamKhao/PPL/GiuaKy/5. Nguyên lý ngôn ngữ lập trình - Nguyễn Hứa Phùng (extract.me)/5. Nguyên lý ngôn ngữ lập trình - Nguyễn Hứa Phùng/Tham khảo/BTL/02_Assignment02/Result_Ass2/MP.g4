grammar MP;
//..........1613166: Nguyen Minh Tham............
@lexer::header {
from lexererr import *

}

options{
	language=Python3;
}
// ..........................................................................................................\\
// ..............................................PARSER.......................................................\\
// ..........................................................................................................\\
// 34 sympol non temneial
program
	: many_decl EOF
	;
many_decl
	: decl many_decl
	| decl
	;
decl
	: var_decl
	| func_decl
	| proce_decl
	;
// Variable Declaration


var_decl
	: VAR many_var_decl
	;

many_var_decl
	: one_var_decl many_var_decl
	| one_var_decl
	;

one_var_decl
	: id_list COLON typeIdentifer  SEMI
	;


// Function Declaration
func_decl
	: FUNCTION ID LB param_list RB COLON typeIdentifer SEMI var_decl? compound_statem
	;

// Procedure Declaration
proce_decl
	: PROCEDURE ID LB param_list RB SEMI var_decl? compound_statem
	;

param_list
	: (param many_param)?
	;

many_param
	: (SEMI param many_param)?
	;

param
	: id_list COLON typeIdentifer
	;

id_list
	: ID (COMMA ID)*
	;

//Type
typeIdentifer
	: primitive_type
	| array_type
	;	
primitive_type
	: BOOLEAN
	| INTEGER
	| REAL
	| STRING
	;

array_type
	: ARRAY LSB sub_intLit DDOT sub_intLit RSB OF primitive_type
	;
sub_intLit
	: SUB? int_literal
	;
// ..........................................................................................................\\
// ..............................................STATEMENT...................................................\\
// ..........................................................................................................\\

statement_type
	: assign_statem
	| if_statem
	| for_statem
	| while_statem
	| break_statem
	| continue_statem
	| call_statem
	| return_statem
	| with_statem
	| compound_statem
	;
many_statement_type
	: (statement_type many_statement_type)?
	;
compound_statem
	: BEGIN many_statement_type END
	;

assign_statem
	: (lhs ASSIGN)+ exp SEMI
	;


lhs
	: ID
	| index_exp
	;


if_statem
	: IF exp THEN statement_type (ELSE statement_type)?
	;

for_statem 
	: FOR ID ASSIGN exp (TO|DOWNTO) exp DO statement_type
	;

//WHILE statement -> OK
while_statem
	: WHILE exp DO statement_type
	;

// Return statement ->OK
return_statem
	: RETURN exp? SEMI
	;

// Return statement ->OK
break_statem
	: BREAK SEMI
	;

// CONTINUE statement ->OK
continue_statem
	: CONTINUE SEMI
	;

// CALL statement ->OK
call_statem
	: ID LB (exp (COMMA exp)*)? RB SEMI
	;

// WITH statement ->OK
with_statem 
	: WITH many_var_decl DO statement_type
	;

// ..........................................................................................................\\
// ..............................................EXPRESSION..................................................\\
// ..........................................................................................................\\
exp
	: exp 	AND THEN 	exp1
    | exp 	OR ELSE 	exp1
    | exp1
    ;
exp1
	: exp2 	EQUAL 		exp2
	| exp2 	NOT_EQUAL 	exp2
	| exp2 	LTHAN 		exp2
	| exp2 	LEQUAL 		exp2
	| exp2 	GTHAN 		exp2
	| exp2 	GEQUAL 		exp2
	| exp2
	;
exp2
	: exp2 	ADD 		exp3
	| exp2 	SUB 		exp3
	| exp2 	OR 			exp3
	| exp3
	;
exp3
	: exp3 	DIVISION 	exp4
	| exp3 	MUL 		exp4
	| exp3 	DIV_INT 	exp4
	| exp3 	MOD 		exp4
	| exp3 	AND			exp4 
	| exp4
	;
exp4: SUB exp4
	| NOT exp4
	| exp5
	;
exp5
	: ID
	| literal
	| LB exp RB
	| index_exp
	| invocation_exp
	;
	
index_exp   //=> exp1 is exp
	: index_exp LSB exp RSB
	| replace_exp LSB exp RSB
	;

replace_exp
	: ID
	| literal
	| invocation_exp
	| LB exp RB
	;

	
invocation_exp
	: ID LB (exp (COMMA exp)*)? RB
	;
// .............................LITERAL......................................\\
literal
	: int_literal
	| float_literal
	| bool_literal
	| string_literal
	;
	
int_literal
	: INT_LITERAL
	;
float_literal
	: FLOAT_LITERAL
	;
bool_literal
	: TRUE 
	| FALSE
	;
string_literal
	: STRING_LITERAL
	;
// ..........................................................................................................\\
// ..............................................LEXER.......................................................\\
// ..........................................................................................................\\
fragment A: 	('a' | 'A') ;
fragment B: 	('b' | 'B') ;
fragment C: 	('c' | 'C') ;
fragment D: 	('d' | 'D') ;
fragment E: 	('e' | 'E') ;
fragment F: 	('f' | 'F') ;
fragment G: 	('g' | 'G') ;
fragment H: 	('h' | 'H') ;
fragment I: 	('i' | 'I') ;
fragment J: 	('j' | 'J') ;
fragment K: 	('k' | 'K') ;
fragment L: 	('l' | 'L') ;
fragment M: 	('m' | 'M') ;
fragment N: 	('n' | 'N') ;
fragment O: 	('o' | 'O') ;
fragment P: 	('p' | 'P') ;
fragment Q: 	('q' | 'Q') ;
fragment R: 	('r' | 'R') ;
fragment S: 	('s' | 'S') ;
fragment T: 	('t' | 'T') ;
fragment U: 	('u' | 'U') ;
fragment V: 	('v' | 'V') ;
fragment W: 	('w' | 'W') ;
fragment X: 	('x' | 'X') ;
fragment Y: 	('y' | 'Y') ;
fragment Z: 	('z' | 'Z') ;

// KEYWORD 
WITH:			W I T H;
BREAK: 			B R E A K ;
CONTINUE: 		C O N T I N U E ;
FOR: 			F O R ;
TO: 			T O ;
DOWNTO: 		D O W N T O ;
DO: 			D O ;
IF: 			I F ;
THEN: 			T H E N ;
ELSE: 			E L S E ;
RETURN: 		R E T U R N ;
WHILE: 			W H I L E ;
BEGIN: 			B E G I N ;
END: 			E N D ;
FUNCTION: 		F U N C T I O N ;
PROCEDURE: 		P R O C E D U R E ;
VAR: 			V A R ;
TRUE: 			T R U E ;
FALSE: 			F A L S E ;
ARRAY: 			A R R A Y ;
OF: 			O F ;
REAL: 			R E A L ;
BOOLEAN: 		B O O L E A N ;
INTEGER: 		I N T E G E R ;
STRING: 		S T R I N G ;

// OPERATORS
ADD: 			'+' ;
SUB: 			'-' ;
MUL: 			'*' ;
DIVISION: 		'/' ;
NOT: 			N O T ;
MOD: 			M O D ;
OR: 			O R ;
AND: 			A N D ;
NOT_EQUAL: 		'<>' ;
EQUAL: 			'=' ;
LTHAN: 			'<' ;
GTHAN: 			'>' ;
LEQUAL: 		'<=' ;
GEQUAL: 		'>=' ;
DIV_INT: 		D I V ;
ASSIGN: 		':=' ;

// SEPARATERS 
LSB: 			'[' ;
RSB: 			']' ;
COLON: 			':' ;
LB: 			'(' ;
RB: 			')' ;
SEMI: 			';';
DDOT: 			'..';
COMMA: 			',' ;

// COMMENTS 
COMMENT_1: 		'(*' .*? '*)' -> skip ;
COMMENT_2:		'{' .*? '}'	-> skip	;
COMMENT_3:		'//' ~[\r\n]* -> skip ;
WS : [ \t\r\n]+ -> skip ; 

//Identifiers
ID: 			[_a-zA-Z] [_a-zA-Z0-9]* ;



//Integer
INT_LITERAL: 	[0-9]+;

//Float
fragment EXPONENT: 	E '-'? [0-9]+;
FLOAT_LITERAL
	: [0-9]+ EXPONENT
	| [0-9]+ '.' ([0-9]* EXPONENT)?
	| [0-9]* '.' [0-9]+ EXPONENT?
	;

//String
fragment ESCAPE_SEQUENCES
	: '\\' [bfrnt'"\\]
	;

STRING_LITERAL
 	: '"' (ESCAPE_SEQUENCES | ~[\n\r'"\\])* '"'
	{
		self.text = self.text[1:-1]
	}
   	; 
	   
ILLEGAL_ESCAPE
 	: '"' (ESCAPE_SEQUENCES | ~[\n\r\b\f\t'"\\])* '\\' (~[bfrnt'"\\] (~'"')*)? '"'
	{

		for x in range(len(self.text)):
			if self.text[x] == '\\':
	  			if (self.text[x+1] == 'b') or (self.text[x+1] == 'f') or (self.text[x+1] == 'r') or (self.text[x+1] == '"n"'):
				    continue
	  			elif (self.text[x+1] == 'n') or (self.text[x+1] == 't') or (self.text[x+1] == '\'') or (self.text[x+1] == '\\'):
				    continue
	  			elif (x+1)==(len(self.text)) :
				    x=x-1
				    break
	  			else:
				    break									
			elif self.text[x] == "\'":
	  			x=x-1
	  			break
		raise IllegalEscape(self.text[1:x+2])
	}
   	;    

UNCLOSE_STRING
 	: '"' (ESCAPE_SEQUENCES| ~[\n\r"\\'] )* [\r\n]?
	{
		raise UncloseString(self.text[1:])
	}
   	;

ERROR_CHAR
 	: .
	{
		raise ErrorToken(self.text[0:])
	}
   	; 