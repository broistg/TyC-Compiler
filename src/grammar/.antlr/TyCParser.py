# Generated from c:/Users/User/Desktop/hoc BK pls/HK252/ppl/BTL/PPL-Project_TyC/src/grammar/TyC.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,5,2,0,7,0,1,0,1,0,1,0,0,0,1,0,0,0,3,0,2,1,0,0,0,2,3,5,0,0,
        1,3,1,1,0,0,0,0
    ]

class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'auto'", "'break'", "'case'", "'continue'", 
                     "'default'", "'else'", "'float'", "'for'", "'if'", 
                     "'int'", "'return'", "'string'", "'struct'", "'switch'", 
                     "'void'", "'while'", "'=='", "'!='", "'<='", "'>='", 
                     "'&&'", "'||'", "'++'", "'--'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'<'", "'>'", "'!'", "'='", "'.'", "'{'", 
                     "'}'", "'('", "')'", "';'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "AUTO", "BREAK", "CASE", "CONTINUE", 
                      "DEFAULT", "ELSE", "FLOAT", "FOR", "IF", "INT", "RETURN", 
                      "STRING", "STRUCT", "SWITCH", "VOID", "WHILE", "EQ", 
                      "NEQ", "LEQ", "GEQ", "AND", "OR", "INCR", "DECR", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "LT", "GT", "NOT", 
                      "ASSIGN", "DOT", "LB", "RB", "LP", "RP", "SEMI", "COMMA", 
                      "COLON", "INTLIT", "FLOATLIT", "STRINGLIT", "ID", 
                      "BLOCK_COMMENT", "LINE_COMMENT", "WS", "ERROR_CHAR", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    AUTO=1
    BREAK=2
    CASE=3
    CONTINUE=4
    DEFAULT=5
    ELSE=6
    FLOAT=7
    FOR=8
    IF=9
    INT=10
    RETURN=11
    STRING=12
    STRUCT=13
    SWITCH=14
    VOID=15
    WHILE=16
    EQ=17
    NEQ=18
    LEQ=19
    GEQ=20
    AND=21
    OR=22
    INCR=23
    DECR=24
    ADD=25
    SUB=26
    MUL=27
    DIV=28
    MOD=29
    LT=30
    GT=31
    NOT=32
    ASSIGN=33
    DOT=34
    LB=35
    RB=36
    LP=37
    RP=38
    SEMI=39
    COMMA=40
    COLON=41
    INTLIT=42
    FLOATLIT=43
    STRINGLIT=44
    ID=45
    BLOCK_COMMENT=46
    LINE_COMMENT=47
    WS=48
    ERROR_CHAR=49
    ILLEGAL_ESCAPE=50
    UNCLOSE_STRING=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TyCParser.EOF, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





