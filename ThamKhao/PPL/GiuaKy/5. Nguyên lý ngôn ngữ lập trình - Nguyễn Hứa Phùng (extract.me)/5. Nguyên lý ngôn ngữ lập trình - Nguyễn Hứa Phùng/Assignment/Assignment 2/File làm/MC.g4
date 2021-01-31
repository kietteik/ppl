grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
    language=Python3;
}

// Program Structure (2)
program: declaration+ EOF;
declaration: vardecls | funcdecls;

// Lexical Specification (3)
// Token Set
//Keywords and Primitive types
BREAK: 'break';
CONTINUE: 'continue';
ELSE: 'else';
FOR: 'for';
IF: 'if';
RETURN: 'return';
DO: 'do';
WHILE: 'while';

BOOLTYPE: 'boolean';
STRINGTYPE: 'string';
FLOATTYPE: 'float';
INTTYPE: 'int';
VOIDTYPE: 'void';

// Operators
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
MODOP: '%';
NOTOP: '!';
OROP: '||';
ANDOP: '&&';
NOTEQUALOP: '!=';
EQUALOP: '==';
LESSOP: '<';
GREATEROP: '>';
LEOREQUOP: '<=';
GROREQUOP: '>=';
ASSIGNOP: '=';
// Separators
LSB: '[';
RSB: ']';
LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';
SEMI: ';';
COMMA: ',';


// Variable declaration

vardecls: primitiveType variables SEMI;
primitiveType: BOOLTYPE | FLOATTYPE | INTTYPE | STRINGTYPE;
variables: var (COMMA var)*;
var: ID | ID LSB INTLIT RSB;

//vardecls: primitiveType var (COMMA var)* SEMI;
//primitiveType: BOOLTYPE | FLOATTYPE | INTTYPE | STRINGTYPE;
//var: ID | ID LSB INTLIT RSB;

// Function declaration
funcdecls: type1 ID LB paraList? RB blockStmt;
type1: primitiveType | VOIDTYPE | arrpointertype;
paraList: paradecls (COMMA paradecls)*;
paradecls: primitiveType ID (LSB RSB)?;


// Literals
INTLIT: [0-9]+;
literals: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT;

FLOATLIT: Fractional | Exponent;
Fractional: (INTLIT? '.' INTLIT) | (INTLIT '.');
Exponent: (Fractional | INTLIT) [Ee] [+-]? INTLIT;
BOOLLIT: TRUE | FALSE;

TRUE: 'true'; // for TRUE and true
FALSE: 'false';
// STRINGLIT: '"' characters '"';
// characters: ~[\b\f\r\n\t\"\\]*;
// characters: ~('\\' [bfrnt"\\])*;
//fragment LEGAL_ESCAPE: '\\' [bfrnt"\\];
//     UNCLOSE_STRING '\\' ~([bfrnt] | '"' | '\\') { raise IllegalEscape(self.text[1:])};

//NEWLINES: '\r'?'\\n';
fragment LEGAL_ESCAPE: '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\\'' | '\\"' | '\\''\\';
STRINGLIT:
    UNCLOSE_STRING '"' {self.text = self.text[1:-1]};
UNCLOSE_STRING:
    '"' (~[\n\r\b\f\t\\"] | LEGAL_ESCAPE)*  {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE:
    UNCLOSE_STRING ('\\' ~[bfrnt"\\]) { raise IllegalEscape(self.text[1:])};

// Types and Values (4)
// Array Pointer Type
arrpointertype: primitiveType ID? LSB RSB;

// Variables (5)
// Expressions (6)
exp: exp1 ASSIGNOP exp | exp1;
exp1: exp1 OROP exp2 | exp2;
exp2: exp2 ANDOP exp3 | exp3;
exp3: exp4 (EQUALOP | NOTEQUALOP) exp4 | exp4;
exp4: exp5 (LESSOP | LEOREQUOP | GREATEROP | GROREQUOP) exp5 | exp5;
exp5: exp5 (ADDOP | SUBOP) exp6 | exp6;
exp6: exp6 (DIVOP | MULOP | MODOP) exp7 | exp7;
exp7: (SUBOP | NOTOP) exp7 | exp8;
exp8: exp9 LSB exp RSB | exp9;
exp9: LB exp RB | exp10;
exp10: operand | funccall;

operand: literals | ID | ID LSB INTLIT RSB;
funccall: ID LB paralist_call? RB;
elementArray: ID LSB INTLIT RSB;
paralist_call: para_call (COMMA para_call)*;
para_call: ID | literals | exp;

// Statements and Control Flow (7)
statement: ifStmt | forStmt | dowhileStmt | breakStmt | continueStmt | returnStmt | expStmt | blockStmt;
ifStmt: IF LB exp RB statement (ELSE statement)?;
dowhileStmt: DO statement+ WHILE exp SEMI;
forStmt: FOR LB exp SEMI exp SEMI exp RB statement;
breakStmt: BREAK SEMI; // for only loops
continueStmt: CONTINUE SEMI; // for only loops
returnStmt: RETURN exp? SEMI;
expStmt: exp SEMI;
blockStmt: LP vardecl_statement* RP;
vardecl_statement: vardecls | statement;

// Identifier
ID: [a-zA-Z_][a-zA-Z_0-9]*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// Comments
BlockComment: '/*' .*? '*/' -> skip;
LineComment: '//' ~[\r\n]* -> skip;

ERROR_CHAR: .;
// UNCLOSE_STRING: .;
// ILLEGAL_ESCAPE: .;