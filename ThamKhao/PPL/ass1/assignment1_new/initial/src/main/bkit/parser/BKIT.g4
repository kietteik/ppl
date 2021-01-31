// ID: 1920069
grammar BKIT;

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

program  : KEY_VAR CL ID SM EOF ;
string: ESCAPE_SEQUENCE;

fragment LOWERCASE  
 : [a-z] 
 ;

fragment UPPERCASE  
 : [A-Z] 
 ;

fragment NUMBER     
 : [0-9] 
 ;

fragment UNDERSCORE     
 : '_' 
 ;

KEY_BODY     
 : 'Body' 
 ;

KEY_BREAK     
 : 'Break' 
 ;

KEY_CONTINUE     
 : 'Continue' 
 ;

KEY_DO     
 : 'Do' 
 ;

KEY_ELSE     
 : 'Else' 
 ;

KEY_ELSEIF     
 : 'ElseIf' 
 ;

KEY_ENDBODY     
 : 'EndBody' 
 ;

KEY_ENDIF     
 : 'EndIf' 
 ;

KEY_ENDFOR     
 : 'EndFor' 
 ;

KEY_ENDWHILE     
 : 'EndWhile' 
 ;

KEY_FOR     
 : 'For' 
 ;

KEY_FUNCTION     
 : 'Function' 
 ;

KEY_IF     
 : 'If' 
 ;

KEY_PARAMETER     
 : 'Parameter' 
 ;

KEY_RETURN     
 : 'Return' 
 ;

KEY_THEN     
 : 'Then' 
 ;

KEY_VAR     
 : 'Var' 
 ;

KEY_WHILE     
 : 'While' 
 ;

KEY_TRUE     
 : 'True' 
 ;

KEY_FALSE     
 : 'False' 
 ;

LSB
   : '['
   ;


RSB
   : ']'
   ;

LP
   : '('
   ;


RP
   : ')'
   ;

CL
   : ':'
   ;

DOT
   : '.'
   ;

CM
   : ','
   ;

SM
   : ';'
   ;

DECIMAL
 : NUMBER+
 ;

HEX
 : '0'[xX] (NUMBER | [A-F])+
 ;

OCTAL
 : '0'[oO] [0-7]+
 ;

INTLIT
 : DECIMAL
 | HEX
 | OCTAL
 ;

FLOATLIT
 : NUMBER+ (DOT NUMBER*)* ([eE] [-+]* NUMBER+)+
 | NUMBER+ (DOT NUMBER*)+ ([eE] [-+]* NUMBER+)*
 | NUMBER+ (DOT NUMBER*)+ ([eE] [-+]* NUMBER+)+
 ;

BOOL
 : KEY_TRUE
 | KEY_FALSE
 ;

ESCAPE_SEQUENCE
 : '\\b'
 | '\\f'
 | '\\r'
 | '\\n'
 | '\\t'
 | '\\\''
 | '\\\\'
 ;

STRINGLIT
 : UNCLOSE_STRING '"'
 ;

ID: LOWERCASE(UPPERCASE | LOWERCASE | UNDERSCORE | NUMBER)* ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


// ERROR_CHAR
//  : '"' EOF STRING_BODY '"'
//  | '"' STRING_BODY EOF'"'
//  | '"' EOF STRING_BODY EOF'"'
//  ;
// UNCLOSE_STRING: '"' (~["])* ESCAPE_SEQUENCE*;
// ILLEGAL_ESCAPE: '"' (~["] | ~ESCAPE_SEQUENCE) '"';
ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;