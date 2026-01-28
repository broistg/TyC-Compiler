grammar TyC;

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
	language = Python3;
}

// -- PARSER RULES --

// Program Structure
program: (structDecl | funcDecl)+ EOF;

// Struct & Function Declarations
structDecl: STRUCT ID LB memberDecl* RB SEMI;
memberDecl: explicitType ID SEMI;

funcDecl: returnType? ID LP paramList? RP blockStmt;
paramList: param (COMMA param)*;
param: explicitType ID;
blockStmt: LB stmt* RB;

// Statements
stmt:
	ifStmt			# ifStmt
	| forStmt		# forStmt
	| whileStmt		# whileStmt
	| switchStmt	# switchStmt
	| breakStmt		# breakStmt
	| continueStmt	# continueStmt
	| returnStmt	# returnStmt
	| blockStmt		# blockStmt
	| varDeclStmt	# varDeclStmt
	| exprStmt		# exprStmt;

varDeclStmt: varType ID (ASSIGN expr)? SEMI;

// Expressions
expr: 'expr'; // Placeholder for expression rules

// Primitive Types
explicitType: INT | FLOAT | STRING | ID;
returnType: VOID | explicitType;
varType: AUTO | explicitType;

// -- LEXER RULES -- 

// Keywords
AUTO: 'auto';
BREAK: 'break';
CASE: 'case';
CONTINUE: 'continue';
DEFAULT: 'default';
ELSE: 'else';
FLOAT: 'float';
FOR: 'for';
IF: 'if';
INT: 'int';
RETURN: 'return';
STRING: 'string';
STRUCT: 'struct';
SWITCH: 'switch';
VOID: 'void';
WHILE: 'while';

// Operators (Longer matches first)
EQ: '==';
NEQ: '!=';
LEQ: '<=';
GEQ: '>=';
AND: '&&';
OR: '||';
INCR: '++';
DECR: '--';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
LT: '<';
GT: '>';
NOT: '!';
ASSIGN: '=';
DOT: '.';

// Separators
LB: '{';
RB: '}';
LP: '(';
RP: ')';
SEMI: ';';
COMMA: ',';
COLON: ':';

// Literals
FLOATLIT:
	Digit+ '.' Digit* Exponent?
	| '.' Digit+ Exponent?
	| Digit+ Exponent;
fragment Exponent: [eE] [+-]? Digit+;
INTLIT: Digit+;
STRLIT: '"' StrChar* '"' {self.text = self.text[1:-1]};

// Identifiers
ID: [a-zA-Z_] [a-zA-Z0-9_]*;

// Skip rules (block before line comments)
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\f\r\n]+ -> skip; // skip whitespaces

// Error handling rules
ILLEGAL_ESCAPE:
	'"' StrChar* '\\' ~[bfrnt"\\\r\n] {self.text = self.text[1:];};
UNCLOSE_STRING: '"' StrChar* '\\'? {self.text = self.text[1:];};
ERROR_CHAR: .;

// Fragments
fragment Digit: [0-9];
fragment EscapeSeq: '\\' [bfrnt"\\];
fragment StrChar: EscapeSeq | ~["\\\r\n];