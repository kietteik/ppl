grammar MC;
options{
    language=Java;
}
@lexer::header{
    package mc.parser;
}
@parser::header{
    package mc.parser;
}
program:;

HEX: '0'[Xx][0-9A-Fa-f]+ ;
INT: [0-9]+;
IF: 'if';
ID: [a-z]+ ;
WS: [ \t\r\n]+ -> skip;