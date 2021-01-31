grammar MP;
/////------------1613166-----------
@lexer::header {
1613166
from lexererr import *

}

options{
	language=Python3;
}

program
	: declarations+ EOF
	;

declarations
	: var_decl
	| func_decl
	| proce_decl
	;
// Variable Declaration
var_decl_list
	: (var_decl var_decl_list)?
	;

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
	: FUNCTION func_name LB param_list RB COLON typeIdentifer SEMI var_decl_list compound_statem
	;
func_name
	: ID
	;

// Procedure Declaration
proce_decl
	: PROCEDURE proce_name LB param_list RB SEMI var_decl_list compound_statem
	;
proce_name
	: ID
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
	: ID COMMA id_list
	| ID
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
	: ARRAY LSB interger_type DDOT interger_type RSB OF primitive_type
	;
interger_type
	: ('-')? INT_LITERAL 
	;
// ..........................................................................................................\\
// ..............................................STATEMENT...................................................\\
// ..........................................................................................................\\
//Compound statement
compound_statem
	: BEGIN statement_list END
	;	
statement_list
	: (statement_type)*
	;
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


//Assignment statement ->OK
assign_statem
	: ((ID | index_exp) ASSIGN)+ exp SEMI
	;


// IF statement

if_statem
	: IF exp THEN statement_type (ELSE statement_type)?
	;

// FOR statement ->OK
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
	: invocation_exp SEMI
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
	| exp3 	DIV_INT		exp4 
	| exp4
	;
exp4: SUB exp4
	| NOT exp4
	| exp5
	;
exp5
	: ID
	| INT_LITERAL
	| FLOAT_LITERAL
	| STRING_LITERAL
	| bool_literal
	| LB exp RB
	| index_exp
	| invocation_exp
	;
	
index_exp   //=> exp1 is exp
	: first_exp (LSB exp RSB)+
	;

first_exp
	: ID
	| INT_LITERAL
	| FLOAT_LITERAL
	| STRING_LITERAL
	| bool_literal
	| invocation_exp
	| LB exp RB
	;
bool_literal
	: TRUE | FALSE
	;
invocation_exp
	: ID LB argument_list RB
	;
argument_list
	: (exp (COMMA exp)*)?
	;
/*
 *
 *		LEXER
 *
 */ 
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