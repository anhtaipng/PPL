grammar BKIT;
/*
MSSV: 1813897
Ho Ten: Pham Nguyen Anh Tai
*/

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

program: vardecl* funcdecl* EOF;

vardecl: VAR COL varlist SM;
varlist: variable ( CM variable)*;
variable: (ID | compositevar) | (ID | compositevar) EQ literal ;
compositevar: ID (LSB INTLIT RSB)*; 

funcdecl: FUNCTION COL ID (PARAM COL paramlist)? BODY COL vardecl* stmt* ENDBODY DOT;
paramlist: param (CM param)*;
param: ID | compositevar;

stmt: assignstmt | ifstmt | forstmt | whilestmt | dostmt | breakstmt | continuestmt | callstmt | returnstmt;

assignstmt: lhs EQ expr SM;
lhs: ID | eleexpr; 
//lhs
eleexpr:  (ID | callexpr)  afterexpr;
afterexpr: (LSB expr RSB)+;


ifstmt: IF expr THEN vardecl* stmt* elifstmt*  elsestmt? ENDIF DOT;
elifstmt: ELSEIF expr THEN vardecl* stmt*;
elsestmt: ELSE vardecl* stmt*;


forstmt: FOR LB ID EQ expr CM expr CM expr RB DO vardecl* stmt* ENDFOR DOT;

whilestmt: WHILE expr DO vardecl* stmt* ENDWHILE DOT;

dostmt: DO vardecl* stmt* WHILE expr ENDDO DOT;

breakstmt: BREAK SM;

continuestmt: CONTINUE SM;


callexpr: ID LB lstcallexpr? RB;
lstcallexpr: expr (CM expr)*;

callstmt: ID LB (expr (CM expr)*)? RB SM;

returnstmt: RETURN expr? SM;




expr: expr1 ( EQEQ | NOTEQ | LT | GT | LTE | GTE | NOTEQF | LTF | GTF | LTEF | GTEF) expr1 | expr1;
expr1: expr1 ( CNJ | DSJ ) expr2 | expr2;
expr2: expr2 ( ADD | SUB | ADDF | SUBF ) expr3 | expr3;
expr3: expr3 ( MUL | MULF | DIV | DIVF | MOD ) expr4 | expr4;
expr4: NEG expr4 | expr5;
expr5: ( SUB | SUBF ) expr5 | expr6;
expr6: expr6 (LSB expr RSB)+ | operand;
operand: ID | literal | LB expr RB | callexpr;



ADD: '+';
SUB: '-';
MUL: '*';
DIV: '\\';
ADDF: '+.';
SUBF: '-.';
MULF: '*.';
DIVF: '\\.';
MOD: '%';
NEG: '!';
CNJ: '&&';
DSJ: '||';

EQEQ: '==';
NOTEQ: '!=';
LT: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
NOTEQF: '=/=';
LTF: '<.';
GTF: '>.';
LTEF: '<=.';
GTEF: '>=.';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines




COMMENT: '**' .*? '**' -> skip;

fragment Lowletter: [a-z];
fragment Letter: [a-zA-Z_];
fragment Digit: [0-9];

ID: Lowletter (Letter | Digit)*;


INTLIT: '0' | [1-9]Digit* | '0'[xX][1-9A-F][0-9A-F]* | '0'[oO][1-7][0-7]*;

fragment Expo: [eE][+-]?Digit*;
FLOATLIT: INTLIT'.'([0]* INTLIT)? Expo? | INTLIT Expo;

boollit: TRUE | FALSE;

fragment EscapeCharacter: '\\' [brtnf'\\];
STRINGLIT: '"' (EscapeCharacter | ~['"\n\\] | '\'"')*? '"'
    {self.text = self.text[1:-1]};


array: LP literal ?  ( CM literal )* RP ;
literal: INTLIT | FLOATLIT | boollit  | STRINGLIT | array;


BODY: 'Body';
BREAK: 'Break';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDBODY: 'EndBody';
ENDIF: 'EndIf';
ENDFOR: 'EndFor';
ENDWHILE:'EndWhile';
FOR: 'For';
FUNCTION: 'Function';
IF: 'If';
MAIN: 'main';
PARAM: 'Parameter';
RETURN: 'Return';
THEN: 'Then';
VAR: 'Var';
WHILE: 'While';
TRUE: 'True';
FALSE: 'False';
ENDDO: 'EndDo';
LP: '{'; RP: '}';
LB: '(' ; RB: ')' ;
LSB: '[' ; RSB: ']' ;
SM: ';' ;
CM: ',' ;
COL: ':';
EQ: '=';
DOT: '.';





ERROR_CHAR: .;
UNCLOSE_STRING:  '"' (EscapeCharacter | ~['"\n\\] | '\'"')* 
{ self.text = self.text[1:];};
ILLEGAL_ESCAPE: '"' (EscapeCharacter | ~['"\n\\] | '\'"')*? ('\\' ~[ntrbf'"\\] | '\'' ~["])
{ self.text = self.text[1:];};
UNTERMINATED_COMMENT: '**' .*? ;