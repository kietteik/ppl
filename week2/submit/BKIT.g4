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

program: VAR COLON ID SEMI EOF;

fragment Num: [0-9];
fragment Letter: [a-z];

ID: Letter (Letter | Num)*;

fragment Part: [eE] [+-]? Num+;
REAL: (Num+ Part) | (Num+ '.' Num+ (Part)?);

STRING: '\'' (~'\'' | '\'' '\'')* '\'';

SEMI: ';';

COLON: ':';

VAR: 'Var';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;