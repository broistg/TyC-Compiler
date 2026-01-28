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

// --- PARSER RULES ---

// Program Structure
program: (structDecl | funcDecl)+ EOF;

// Struct & Function Declarations
structDecl: STRUCT ID LB memberDecl* RB SEMI;
memberDecl: explicitType ID SEMI;

funcDecl: returnType? ID LP paramList? RP block;
paramList: param (COMMA param)*;
param: explicitType ID;

// Statements
stmt:
	IF LP expr RP stmt (ELSE stmt)?				# IfStmt
	| WHILE LP expr RP stmt						# WhileStmt
	| FOR LP forInit expr? SEMI expr? RP stmt	# ForStmt
	| SWITCH LP expr RP LB switchCase* RB		# SwitchStmt
	| BREAK SEMI								# BreakStmt
	| CONTINUE SEMI								# ContinueStmt
	| RETURN expr? SEMI							# ReturnStmt
	| block										# BlockStmt
	| varDecl									# VarDeclStmt
	| expr SEMI									# ExprStmt;

block: LB stmt* RB; // Block helper
varDecl: varType ID (ASSIGN expr)? SEMI; // Variable declaration
forInit: varDecl | expr? SEMI; // Helper for for statement
switchCase: (CASE expr COLON | DEFAULT COLON)+ stmt*; // Switch cases

// Expressions
expr:
	// Level 1: Primary Expressions (Highest Priority)
	ID LP exprList? RP	# FuncCall
	| LB exprList? RB	# StructLiteral
	| ID				# IdExpr
	| INTLIT			# IntLitExpr
	| FLOATLIT			# FloatLitExpr
	| STRLIT			# StringLitExpr
	| LP expr RP		# ParentExpr

	// Level 2: Member Access (Left Associative)
	| expr DOT ID # MemberAccess

	// Level 3: Postfix Operators (Left Associative)
	| expr (INCR | DECR) # PostfixExpr

	// Level 4: Prefix Operators (Right Associative)
	| (INCR | DECR) expr # PrefixExpr

	// Level 5: Unary Operators (Right Associative)
	| (NOT | SUB | ADD) expr # UnaryExpr

	// Level 6: Multiplicative (Left Associative)
	| expr (MUL | DIV | MOD) expr # BinaryOp

	// Level 7: Additive (Left Associative)
	| expr (ADD | SUB) expr # BinaryOp

	// Level 8: Relational (Left Associative)
	| expr (LT | LEQ | GT | GEQ) expr # BinaryOp

	// Level 9: Equality (Left Associative)
	| expr (EQ | NEQ) expr # BinaryOp

	// Level 10: Logical AND (Left Associative)
	| expr AND expr # BinaryOp

	// Level 11: Logical OR (Left Associative)
	| expr OR expr # BinaryOp

	// Level 12: Assignment (Right Associative)
	| <assoc = right> expr ASSIGN expr # AssignExpr;

exprList:
	expr (COMMA expr)*; // Helper for function calls and struct literals

// Primitive Types
explicitType: INT | FLOAT | STRING | ID;
returnType: VOID | explicitType;
varType: AUTO | explicitType;

// --- LEXER RULES ---

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

// Skip rules (match block comments before line comments)
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