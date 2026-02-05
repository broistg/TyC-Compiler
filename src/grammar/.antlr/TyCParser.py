# Generated from c:/Users/User/Desktop/hoc BK pls/HK252/PPL/BTL/TyC-Compiler/src/grammar/TyC.g4 by ANTLR 4.13.1
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
        4,1,51,252,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,5,0,35,8,0,10,0,12,0,38,9,0,1,0,1,0,
        1,1,1,1,1,1,1,1,5,1,46,8,1,10,1,12,1,49,9,1,1,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,3,3,3,59,8,3,1,3,1,3,1,3,3,3,64,8,3,1,3,1,3,1,3,1,4,1,
        4,1,4,5,4,72,8,4,10,4,12,4,75,9,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,3,6,87,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,
        99,8,6,1,6,1,6,3,6,103,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,
        6,114,8,6,10,6,12,6,117,9,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,
        127,8,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,135,8,6,1,7,1,7,5,7,139,8,7,
        10,7,12,7,142,9,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,150,8,8,1,8,1,8,1,
        9,1,9,3,9,156,8,9,1,9,3,9,159,8,9,1,10,1,10,1,10,1,10,1,10,1,10,
        4,10,167,8,10,11,10,12,10,168,1,10,5,10,172,8,10,10,10,12,10,175,
        9,10,1,11,1,11,1,11,1,11,3,11,181,8,11,1,11,1,11,1,11,3,11,186,8,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,3,11,201,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,5,11,229,8,11,10,11,12,11,232,9,11,1,12,1,12,1,
        12,5,12,237,8,12,10,12,12,12,240,9,12,1,13,1,13,1,14,1,14,3,14,246,
        8,14,1,15,1,15,3,15,250,8,15,1,15,0,1,22,16,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,0,7,1,0,23,24,2,0,25,26,32,32,1,0,27,29,1,0,
        25,26,2,0,19,20,30,31,1,0,17,18,4,0,7,7,10,10,12,12,45,45,284,0,
        36,1,0,0,0,2,41,1,0,0,0,4,53,1,0,0,0,6,58,1,0,0,0,8,68,1,0,0,0,10,
        76,1,0,0,0,12,134,1,0,0,0,14,136,1,0,0,0,16,145,1,0,0,0,18,158,1,
        0,0,0,20,166,1,0,0,0,22,200,1,0,0,0,24,233,1,0,0,0,26,241,1,0,0,
        0,28,245,1,0,0,0,30,249,1,0,0,0,32,35,3,2,1,0,33,35,3,6,3,0,34,32,
        1,0,0,0,34,33,1,0,0,0,35,38,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,
        37,39,1,0,0,0,38,36,1,0,0,0,39,40,5,0,0,1,40,1,1,0,0,0,41,42,5,13,
        0,0,42,43,5,45,0,0,43,47,5,35,0,0,44,46,3,4,2,0,45,44,1,0,0,0,46,
        49,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,1,0,0,
        0,50,51,5,36,0,0,51,52,5,39,0,0,52,3,1,0,0,0,53,54,3,26,13,0,54,
        55,5,45,0,0,55,56,5,39,0,0,56,5,1,0,0,0,57,59,3,28,14,0,58,57,1,
        0,0,0,58,59,1,0,0,0,59,60,1,0,0,0,60,61,5,45,0,0,61,63,5,37,0,0,
        62,64,3,8,4,0,63,62,1,0,0,0,63,64,1,0,0,0,64,65,1,0,0,0,65,66,5,
        38,0,0,66,67,3,14,7,0,67,7,1,0,0,0,68,73,3,10,5,0,69,70,5,40,0,0,
        70,72,3,10,5,0,71,69,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,
        0,0,0,74,9,1,0,0,0,75,73,1,0,0,0,76,77,3,26,13,0,77,78,5,45,0,0,
        78,11,1,0,0,0,79,80,5,9,0,0,80,81,5,37,0,0,81,82,3,22,11,0,82,83,
        5,38,0,0,83,86,3,12,6,0,84,85,5,6,0,0,85,87,3,12,6,0,86,84,1,0,0,
        0,86,87,1,0,0,0,87,135,1,0,0,0,88,89,5,16,0,0,89,90,5,37,0,0,90,
        91,3,22,11,0,91,92,5,38,0,0,92,93,3,12,6,0,93,135,1,0,0,0,94,95,
        5,8,0,0,95,96,5,37,0,0,96,98,3,18,9,0,97,99,3,22,11,0,98,97,1,0,
        0,0,98,99,1,0,0,0,99,100,1,0,0,0,100,102,5,39,0,0,101,103,3,22,11,
        0,102,101,1,0,0,0,102,103,1,0,0,0,103,104,1,0,0,0,104,105,5,38,0,
        0,105,106,3,12,6,0,106,135,1,0,0,0,107,108,5,14,0,0,108,109,5,37,
        0,0,109,110,3,22,11,0,110,111,5,38,0,0,111,115,5,35,0,0,112,114,
        3,20,10,0,113,112,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,
        1,0,0,0,116,118,1,0,0,0,117,115,1,0,0,0,118,119,5,36,0,0,119,135,
        1,0,0,0,120,121,5,2,0,0,121,135,5,39,0,0,122,123,5,4,0,0,123,135,
        5,39,0,0,124,126,5,11,0,0,125,127,3,22,11,0,126,125,1,0,0,0,126,
        127,1,0,0,0,127,128,1,0,0,0,128,135,5,39,0,0,129,135,3,14,7,0,130,
        135,3,16,8,0,131,132,3,22,11,0,132,133,5,39,0,0,133,135,1,0,0,0,
        134,79,1,0,0,0,134,88,1,0,0,0,134,94,1,0,0,0,134,107,1,0,0,0,134,
        120,1,0,0,0,134,122,1,0,0,0,134,124,1,0,0,0,134,129,1,0,0,0,134,
        130,1,0,0,0,134,131,1,0,0,0,135,13,1,0,0,0,136,140,5,35,0,0,137,
        139,3,12,6,0,138,137,1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,
        141,1,0,0,0,141,143,1,0,0,0,142,140,1,0,0,0,143,144,5,36,0,0,144,
        15,1,0,0,0,145,146,3,30,15,0,146,149,5,45,0,0,147,148,5,33,0,0,148,
        150,3,22,11,0,149,147,1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,
        152,5,39,0,0,152,17,1,0,0,0,153,159,3,16,8,0,154,156,3,22,11,0,155,
        154,1,0,0,0,155,156,1,0,0,0,156,157,1,0,0,0,157,159,5,39,0,0,158,
        153,1,0,0,0,158,155,1,0,0,0,159,19,1,0,0,0,160,161,5,3,0,0,161,162,
        3,22,11,0,162,163,5,41,0,0,163,167,1,0,0,0,164,165,5,5,0,0,165,167,
        5,41,0,0,166,160,1,0,0,0,166,164,1,0,0,0,167,168,1,0,0,0,168,166,
        1,0,0,0,168,169,1,0,0,0,169,173,1,0,0,0,170,172,3,12,6,0,171,170,
        1,0,0,0,172,175,1,0,0,0,173,171,1,0,0,0,173,174,1,0,0,0,174,21,1,
        0,0,0,175,173,1,0,0,0,176,177,6,11,-1,0,177,178,5,45,0,0,178,180,
        5,37,0,0,179,181,3,24,12,0,180,179,1,0,0,0,180,181,1,0,0,0,181,182,
        1,0,0,0,182,201,5,38,0,0,183,185,5,35,0,0,184,186,3,24,12,0,185,
        184,1,0,0,0,185,186,1,0,0,0,186,187,1,0,0,0,187,201,5,36,0,0,188,
        201,5,45,0,0,189,201,5,43,0,0,190,201,5,42,0,0,191,201,5,44,0,0,
        192,193,5,37,0,0,193,194,3,22,11,0,194,195,5,38,0,0,195,201,1,0,
        0,0,196,197,7,0,0,0,197,201,3,22,11,9,198,199,7,1,0,0,199,201,3,
        22,11,8,200,176,1,0,0,0,200,183,1,0,0,0,200,188,1,0,0,0,200,189,
        1,0,0,0,200,190,1,0,0,0,200,191,1,0,0,0,200,192,1,0,0,0,200,196,
        1,0,0,0,200,198,1,0,0,0,201,230,1,0,0,0,202,203,10,7,0,0,203,204,
        7,2,0,0,204,229,3,22,11,8,205,206,10,6,0,0,206,207,7,3,0,0,207,229,
        3,22,11,7,208,209,10,5,0,0,209,210,7,4,0,0,210,229,3,22,11,6,211,
        212,10,4,0,0,212,213,7,5,0,0,213,229,3,22,11,5,214,215,10,3,0,0,
        215,216,5,21,0,0,216,229,3,22,11,4,217,218,10,2,0,0,218,219,5,22,
        0,0,219,229,3,22,11,3,220,221,10,1,0,0,221,222,5,33,0,0,222,229,
        3,22,11,1,223,224,10,11,0,0,224,225,5,34,0,0,225,229,5,45,0,0,226,
        227,10,10,0,0,227,229,7,0,0,0,228,202,1,0,0,0,228,205,1,0,0,0,228,
        208,1,0,0,0,228,211,1,0,0,0,228,214,1,0,0,0,228,217,1,0,0,0,228,
        220,1,0,0,0,228,223,1,0,0,0,228,226,1,0,0,0,229,232,1,0,0,0,230,
        228,1,0,0,0,230,231,1,0,0,0,231,23,1,0,0,0,232,230,1,0,0,0,233,238,
        3,22,11,0,234,235,5,40,0,0,235,237,3,22,11,0,236,234,1,0,0,0,237,
        240,1,0,0,0,238,236,1,0,0,0,238,239,1,0,0,0,239,25,1,0,0,0,240,238,
        1,0,0,0,241,242,7,6,0,0,242,27,1,0,0,0,243,246,5,15,0,0,244,246,
        3,26,13,0,245,243,1,0,0,0,245,244,1,0,0,0,246,29,1,0,0,0,247,250,
        5,1,0,0,248,250,3,26,13,0,249,247,1,0,0,0,249,248,1,0,0,0,250,31,
        1,0,0,0,27,34,36,47,58,63,73,86,98,102,115,126,134,140,149,155,158,
        166,168,173,180,185,200,228,230,238,245,249
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
                      "COLON", "FLOATLIT", "INTLIT", "STRLIT", "ID", "BLOCK_COMMENT", 
                      "LINE_COMMENT", "WS", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_structDecl = 1
    RULE_memberDecl = 2
    RULE_funcDecl = 3
    RULE_paramList = 4
    RULE_param = 5
    RULE_stmt = 6
    RULE_block = 7
    RULE_varDecl = 8
    RULE_forInit = 9
    RULE_switchCase = 10
    RULE_expr = 11
    RULE_exprList = 12
    RULE_explicitType = 13
    RULE_returnType = 14
    RULE_varType = 15

    ruleNames =  [ "program", "structDecl", "memberDecl", "funcDecl", "paramList", 
                   "param", "stmt", "block", "varDecl", "forInit", "switchCase", 
                   "expr", "exprList", "explicitType", "returnType", "varType" ]

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
    FLOATLIT=42
    INTLIT=43
    STRLIT=44
    ID=45
    BLOCK_COMMENT=46
    LINE_COMMENT=47
    WS=48
    ILLEGAL_ESCAPE=49
    UNCLOSE_STRING=50
    ERROR_CHAR=51

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

        def structDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StructDeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.StructDeclContext,i)


        def funcDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.FuncDeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.FuncDeclContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372135040) != 0):
                self.state = 34
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [13]:
                    self.state = 32
                    self.structDecl()
                    pass
                elif token in [7, 10, 12, 15, 45]:
                    self.state = 33
                    self.funcDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(TyCParser.STRUCT, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LB(self):
            return self.getToken(TyCParser.LB, 0)

        def RB(self):
            return self.getToken(TyCParser.RB, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def memberDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.MemberDeclContext)
            else:
                return self.getTypedRuleContext(TyCParser.MemberDeclContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_structDecl




    def structDecl(self):

        localctx = TyCParser.StructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_structDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(TyCParser.STRUCT)
            self.state = 42
            self.match(TyCParser.ID)
            self.state = 43
            self.match(TyCParser.LB)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372094080) != 0):
                self.state = 44
                self.memberDecl()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(TyCParser.RB)
            self.state = 51
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explicitType(self):
            return self.getTypedRuleContext(TyCParser.ExplicitTypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_memberDecl




    def memberDecl(self):

        localctx = TyCParser.MemberDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_memberDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.explicitType()
            self.state = 54
            self.match(TyCParser.ID)
            self.state = 55
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)

        def RP(self):
            return self.getToken(TyCParser.RP, 0)

        def block(self):
            return self.getTypedRuleContext(TyCParser.BlockContext,0)


        def returnType(self):
            return self.getTypedRuleContext(TyCParser.ReturnTypeContext,0)


        def paramList(self):
            return self.getTypedRuleContext(TyCParser.ParamListContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_funcDecl




    def funcDecl(self):

        localctx = TyCParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 57
                self.returnType()


            self.state = 60
            self.match(TyCParser.ID)
            self.state = 61
            self.match(TyCParser.LP)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372094080) != 0):
                self.state = 62
                self.paramList()


            self.state = 65
            self.match(TyCParser.RP)
            self.state = 66
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ParamContext)
            else:
                return self.getTypedRuleContext(TyCParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_paramList




    def paramList(self):

        localctx = TyCParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.param()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 69
                self.match(TyCParser.COMMA)
                self.state = 70
                self.param()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explicitType(self):
            return self.getTypedRuleContext(TyCParser.ExplicitTypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_param




    def param(self):

        localctx = TyCParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.explicitType()
            self.state = 77
            self.match(TyCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TyCParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ContinueStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONTINUE(self):
            return self.getToken(TyCParser.CONTINUE, 0)
        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)


    class SwitchStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SWITCH(self):
            return self.getToken(TyCParser.SWITCH, 0)
        def LP(self):
            return self.getToken(TyCParser.LP, 0)
        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def RP(self):
            return self.getToken(TyCParser.RP, 0)
        def LB(self):
            return self.getToken(TyCParser.LB, 0)
        def RB(self):
            return self.getToken(TyCParser.RB, 0)
        def switchCase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.SwitchCaseContext)
            else:
                return self.getTypedRuleContext(TyCParser.SwitchCaseContext,i)



    class IfStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(TyCParser.IF, 0)
        def LP(self):
            return self.getToken(TyCParser.LP, 0)
        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def RP(self):
            return self.getToken(TyCParser.RP, 0)
        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)

        def ELSE(self):
            return self.getToken(TyCParser.ELSE, 0)


    class ExprStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)


    class WhileStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(TyCParser.WHILE, 0)
        def LP(self):
            return self.getToken(TyCParser.LP, 0)
        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def RP(self):
            return self.getToken(TyCParser.RP, 0)
        def stmt(self):
            return self.getTypedRuleContext(TyCParser.StmtContext,0)



    class BreakStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BREAK(self):
            return self.getToken(TyCParser.BREAK, 0)
        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)


    class VarDeclStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def varDecl(self):
            return self.getTypedRuleContext(TyCParser.VarDeclContext,0)



    class BlockStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def block(self):
            return self.getTypedRuleContext(TyCParser.BlockContext,0)



    class ForStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(TyCParser.FOR, 0)
        def LP(self):
            return self.getToken(TyCParser.LP, 0)
        def forInit(self):
            return self.getTypedRuleContext(TyCParser.ForInitContext,0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)
        def RP(self):
            return self.getToken(TyCParser.RP, 0)
        def stmt(self):
            return self.getTypedRuleContext(TyCParser.StmtContext,0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)



    class ReturnStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(TyCParser.RETURN, 0)
        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)
        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)




    def stmt(self):

        localctx = TyCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = TyCParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(TyCParser.IF)
                self.state = 80
                self.match(TyCParser.LP)
                self.state = 81
                self.expr(0)
                self.state = 82
                self.match(TyCParser.RP)
                self.state = 83
                self.stmt()
                self.state = 86
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 84
                    self.match(TyCParser.ELSE)
                    self.state = 85
                    self.stmt()


                pass

            elif la_ == 2:
                localctx = TyCParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.match(TyCParser.WHILE)
                self.state = 89
                self.match(TyCParser.LP)
                self.state = 90
                self.expr(0)
                self.state = 91
                self.match(TyCParser.RP)
                self.state = 92
                self.stmt()
                pass

            elif la_ == 3:
                localctx = TyCParser.ForStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.match(TyCParser.FOR)
                self.state = 95
                self.match(TyCParser.LP)
                self.state = 96
                self.forInit()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66146917154816) != 0):
                    self.state = 97
                    self.expr(0)


                self.state = 100
                self.match(TyCParser.SEMI)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66146917154816) != 0):
                    self.state = 101
                    self.expr(0)


                self.state = 104
                self.match(TyCParser.RP)
                self.state = 105
                self.stmt()
                pass

            elif la_ == 4:
                localctx = TyCParser.SwitchStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 107
                self.match(TyCParser.SWITCH)
                self.state = 108
                self.match(TyCParser.LP)
                self.state = 109
                self.expr(0)
                self.state = 110
                self.match(TyCParser.RP)
                self.state = 111
                self.match(TyCParser.LB)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3 or _la==5:
                    self.state = 112
                    self.switchCase()
                    self.state = 117
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 118
                self.match(TyCParser.RB)
                pass

            elif la_ == 5:
                localctx = TyCParser.BreakStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 120
                self.match(TyCParser.BREAK)
                self.state = 121
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 6:
                localctx = TyCParser.ContinueStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 122
                self.match(TyCParser.CONTINUE)
                self.state = 123
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 7:
                localctx = TyCParser.ReturnStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 124
                self.match(TyCParser.RETURN)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66146917154816) != 0):
                    self.state = 125
                    self.expr(0)


                self.state = 128
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 8:
                localctx = TyCParser.BlockStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 129
                self.block()
                pass

            elif la_ == 9:
                localctx = TyCParser.VarDeclStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 130
                self.varDecl()
                pass

            elif la_ == 10:
                localctx = TyCParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 131
                self.expr(0)
                self.state = 132
                self.match(TyCParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(TyCParser.LB, 0)

        def RB(self):
            return self.getToken(TyCParser.RB, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_block




    def block(self):

        localctx = TyCParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(TyCParser.LB)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 66146917244822) != 0):
                self.state = 137
                self.stmt()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
            self.match(TyCParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varType(self):
            return self.getTypedRuleContext(TyCParser.VarTypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_varDecl




    def varDecl(self):

        localctx = TyCParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.varType()
            self.state = 146
            self.match(TyCParser.ID)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 147
                self.match(TyCParser.ASSIGN)
                self.state = 148
                self.expr(0)


            self.state = 151
            self.match(TyCParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDecl(self):
            return self.getTypedRuleContext(TyCParser.VarDeclContext,0)


        def SEMI(self):
            return self.getToken(TyCParser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forInit




    def forInit(self):

        localctx = TyCParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forInit)
        self._la = 0 # Token type
        try:
            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66146917154816) != 0):
                    self.state = 154
                    self.expr(0)


                self.state = 157
                self.match(TyCParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.CASE)
            else:
                return self.getToken(TyCParser.CASE, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COLON)
            else:
                return self.getToken(TyCParser.COLON, i)

        def DEFAULT(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.DEFAULT)
            else:
                return self.getToken(TyCParser.DEFAULT, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StmtContext)
            else:
                return self.getTypedRuleContext(TyCParser.StmtContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_switchCase




    def switchCase(self):

        localctx = TyCParser.SwitchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_switchCase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 166
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3]:
                        self.state = 160
                        self.match(TyCParser.CASE)
                        self.state = 161
                        self.expr(0)
                        self.state = 162
                        self.match(TyCParser.COLON)
                        pass
                    elif token in [5]:
                        self.state = 164
                        self.match(TyCParser.DEFAULT)
                        self.state = 165
                        self.match(TyCParser.COLON)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 168 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 66146917244822) != 0):
                self.state = 170
                self.stmt()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TyCParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StructLiteralContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LB(self):
            return self.getToken(TyCParser.LB, 0)
        def RB(self):
            return self.getToken(TyCParser.RB, 0)
        def exprList(self):
            return self.getTypedRuleContext(TyCParser.ExprListContext,0)



    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)


    class StringLitExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRLIT(self):
            return self.getToken(TyCParser.STRLIT, 0)


    class ParentExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LP(self):
            return self.getToken(TyCParser.LP, 0)
        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def RP(self):
            return self.getToken(TyCParser.RP, 0)


    class UnaryExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def NOT(self):
            return self.getToken(TyCParser.NOT, 0)
        def SUB(self):
            return self.getToken(TyCParser.SUB, 0)
        def ADD(self):
            return self.getToken(TyCParser.ADD, 0)


    class PrefixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def INCR(self):
            return self.getToken(TyCParser.INCR, 0)
        def DECR(self):
            return self.getToken(TyCParser.DECR, 0)


    class AssignExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)


    class PostfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def INCR(self):
            return self.getToken(TyCParser.INCR, 0)
        def DECR(self):
            return self.getToken(TyCParser.DECR, 0)


    class FuncCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)
        def LP(self):
            return self.getToken(TyCParser.LP, 0)
        def RP(self):
            return self.getToken(TyCParser.RP, 0)
        def exprList(self):
            return self.getTypedRuleContext(TyCParser.ExprListContext,0)



    class MemberAccessContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TyCParser.ExprContext,0)

        def DOT(self):
            return self.getToken(TyCParser.DOT, 0)
        def ID(self):
            return self.getToken(TyCParser.ID, 0)


    class IntLitExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INTLIT(self):
            return self.getToken(TyCParser.INTLIT, 0)


    class FloatLitExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOATLIT(self):
            return self.getToken(TyCParser.FLOATLIT, 0)


    class BinaryOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TyCParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)

        def MUL(self):
            return self.getToken(TyCParser.MUL, 0)
        def DIV(self):
            return self.getToken(TyCParser.DIV, 0)
        def MOD(self):
            return self.getToken(TyCParser.MOD, 0)
        def ADD(self):
            return self.getToken(TyCParser.ADD, 0)
        def SUB(self):
            return self.getToken(TyCParser.SUB, 0)
        def LT(self):
            return self.getToken(TyCParser.LT, 0)
        def LEQ(self):
            return self.getToken(TyCParser.LEQ, 0)
        def GT(self):
            return self.getToken(TyCParser.GT, 0)
        def GEQ(self):
            return self.getToken(TyCParser.GEQ, 0)
        def EQ(self):
            return self.getToken(TyCParser.EQ, 0)
        def NEQ(self):
            return self.getToken(TyCParser.NEQ, 0)
        def AND(self):
            return self.getToken(TyCParser.AND, 0)
        def OR(self):
            return self.getToken(TyCParser.OR, 0)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TyCParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = TyCParser.FuncCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 177
                self.match(TyCParser.ID)
                self.state = 178
                self.match(TyCParser.LP)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66146917154816) != 0):
                    self.state = 179
                    self.exprList()


                self.state = 182
                self.match(TyCParser.RP)
                pass

            elif la_ == 2:
                localctx = TyCParser.StructLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 183
                self.match(TyCParser.LB)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66146917154816) != 0):
                    self.state = 184
                    self.exprList()


                self.state = 187
                self.match(TyCParser.RB)
                pass

            elif la_ == 3:
                localctx = TyCParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 188
                self.match(TyCParser.ID)
                pass

            elif la_ == 4:
                localctx = TyCParser.IntLitExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 189
                self.match(TyCParser.INTLIT)
                pass

            elif la_ == 5:
                localctx = TyCParser.FloatLitExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 190
                self.match(TyCParser.FLOATLIT)
                pass

            elif la_ == 6:
                localctx = TyCParser.StringLitExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 191
                self.match(TyCParser.STRLIT)
                pass

            elif la_ == 7:
                localctx = TyCParser.ParentExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 192
                self.match(TyCParser.LP)
                self.state = 193
                self.expr(0)
                self.state = 194
                self.match(TyCParser.RP)
                pass

            elif la_ == 8:
                localctx = TyCParser.PrefixExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 196
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 197
                self.expr(9)
                pass

            elif la_ == 9:
                localctx = TyCParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 198
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4395630592) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 199
                self.expr(8)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 230
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 228
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.BinaryOpContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 202
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 203
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 204
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.BinaryOpContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 205
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 206
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 207
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = TyCParser.BinaryOpContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 208
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 209
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3222798336) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 210
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = TyCParser.BinaryOpContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 211
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 212
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 213
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = TyCParser.BinaryOpContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 214
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 215
                        self.match(TyCParser.AND)
                        self.state = 216
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = TyCParser.BinaryOpContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 217
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 218
                        self.match(TyCParser.OR)
                        self.state = 219
                        self.expr(3)
                        pass

                    elif la_ == 7:
                        localctx = TyCParser.AssignExprContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 220
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 221
                        self.match(TyCParser.ASSIGN)
                        self.state = 222
                        self.expr(1)
                        pass

                    elif la_ == 8:
                        localctx = TyCParser.MemberAccessContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 223
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 224
                        self.match(TyCParser.DOT)
                        self.state = 225
                        self.match(TyCParser.ID)
                        pass

                    elif la_ == 9:
                        localctx = TyCParser.PostfixExprContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 226
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 227
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 232
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExprContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_exprList




    def exprList(self):

        localctx = TyCParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.expr(0)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 234
                self.match(TyCParser.COMMA)
                self.state = 235
                self.expr(0)
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplicitTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_explicitType




    def explicitType(self):

        localctx = TyCParser.ExplicitTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_explicitType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372094080) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(TyCParser.VOID, 0)

        def explicitType(self):
            return self.getTypedRuleContext(TyCParser.ExplicitTypeContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_returnType




    def returnType(self):

        localctx = TyCParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_returnType)
        try:
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(TyCParser.VOID)
                pass
            elif token in [7, 10, 12, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.explicitType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTO(self):
            return self.getToken(TyCParser.AUTO, 0)

        def explicitType(self):
            return self.getTypedRuleContext(TyCParser.ExplicitTypeContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_varType




    def varType(self):

        localctx = TyCParser.VarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_varType)
        try:
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(TyCParser.AUTO)
                pass
            elif token in [7, 10, 12, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 248
                self.explicitType()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 10)
         




