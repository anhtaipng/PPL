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

program: (vardeclpart | funcdeclpart)* EOF;

vardeclpart: vardecl+;
vardecl: VAR COL varlist SM;
varlist: variable ( CM variable)*;
variable: (ID | compositevar) | (ID | compositevar) EQ initvalue ;
initvalue : INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | array;
compositevar: ID (LSB INTLIT RSB)*; 

funcdeclpart: funcdecl+;
funcdecl: FUNCTION COL ID (PARAM COL paramlist)* BODY COL vardecl* stmt* ENDBODY DOT;
paramlist: ID (CM ID)*;

stmt: assignstmt | ifstmt | forstmt | whilestmt | dostmt | breakstmt | continuestmt | callstmt | returnstmt;

assignstmt: (ID | indexexpr) EQ expr SM;

ifstmt: IF expr THEN stmt* (ELSEIF expr THEN stmt*)*  (ELSE stmt*)* ENDIF DOT;

forstmt: FOR forexprs DO stmt* ENDFOR DOT;
forexprs: LB variable EQ initexpr CM conexpr CM updateexpr RB;
initexpr: expr;
conexpr: expr;
updateexpr: expr;

whilestmt: WHILE expr DO stmt* ENDWHILE DOT;

dostmt: DO stmt* WHILE expr ENDDO DOT;

breakstmt: BREAK SM;

continuestmt: CONTINUE SM;

callstmt: callexpr SM;
callexpr: ID LB (expr (CM expr)*)? RB;

returnstmt: RETURN expr? SM;

//unary expr
indexexpr: ID indexoper;
indexoper: LSB expr RSB indexoper*;
signexpr: (SUB | SUBF) expr;
logicexpr: NEG expr;

expr: expr (MUL | MULF | DIV | DIVF | MOD) expr1 | expr1;
expr1: expr1 (ADD | ADDF | SUB |SUBF) expr2 | expr2;
expr2: expr2 (CNJ | DSJ) expr3 | expr3;
expr3: expr3 (EQEQ | NOTEQ | LT | GT | LTE | GTE | NOTEQF | LTF | GTF | LTEF | GTEF) expr4 | expr4;
expr4: ID | INTLIT | FLOATLIT | BOOLLIT | indexexpr | signexpr | logicexpr | LB expr RB | callexpr;


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
FLOATLIT: INTLIT'.'INTLIT?Expo?;

BOOLLIT: TRUE | FALSE;

fragment EscapeCharacter: '\\' [brtnf'\\];
STRINGLIT: '"' (EscapeCharacter | ~['"\n\\] | '\'"')*? '"'
    {self.text = self.text[1:-1]};


array: LP  (INTLIT | FLOATLIT | BOOLLIT  | STRINGLIT | array)?  ( CM (INTLIT | FLOATLIT | BOOLLIT  | STRINGLIT | array))* RP ;


BODY: 'Body';
BREAK: 'Break';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDBODY: 'EndBody';
ENDIF: 'EndIf';
ENDFOR: 'EndFor';
ENDWHILE:' EndWhile';
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