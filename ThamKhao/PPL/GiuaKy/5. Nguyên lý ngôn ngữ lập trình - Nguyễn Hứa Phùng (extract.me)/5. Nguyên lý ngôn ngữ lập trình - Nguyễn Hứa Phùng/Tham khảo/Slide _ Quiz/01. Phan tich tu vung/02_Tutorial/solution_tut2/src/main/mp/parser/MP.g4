grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : mptype 'main' LB RB LP body? RP EOF ;

mptype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;

INTTYPE: 'int' ;

VOIDTYPE: 'void'  ;

//Câu 1
//ID: [a-z] [0-9a-z]*;

//Câu 2
fragment LETTER: [a-z];
fragment NUMBER: [0-9];
ID: LETTER (NUMBER | LETTER)+;

//Câu 3a:
REAL: [0-9]+ ('.')? [0-9]* [eE]? ('-')? [0-9]+;

STRINGLIT: '\''		(~['])*	'\''	
		{
			self.text = self.text[1:-1]
		}
		;


INTLIT: [0-9]+;



LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;