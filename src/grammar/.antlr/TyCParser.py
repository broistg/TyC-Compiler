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
        4,1,51,251,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,4,0,35,8,0,11,0,12,0,36,1,0,1,0,1,1,
        1,1,1,1,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,1,1,1,1,1,1,2,1,2,1,2,
        1,2,1,3,3,3,58,8,3,1,3,1,3,1,3,3,3,63,8,3,1,3,1,3,1,3,1,4,1,4,1,
        4,5,4,71,8,4,10,4,12,4,74,9,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,3,6,86,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,98,
        8,6,1,6,1,6,3,6,102,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,
        113,8,6,10,6,12,6,116,9,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,126,
        8,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,134,8,6,1,7,1,7,5,7,138,8,7,10,7,
        12,7,141,9,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,149,8,8,1,8,1,8,1,9,1,9,
        3,9,155,8,9,1,9,3,9,158,8,9,1,10,1,10,1,10,1,10,1,10,1,10,4,10,166,
        8,10,11,10,12,10,167,1,10,5,10,171,8,10,10,10,12,10,174,9,10,1,11,
        1,11,1,11,1,11,3,11,180,8,11,1,11,1,11,1,11,3,11,185,8,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,200,
        8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,5,11,228,8,11,10,11,12,11,231,9,11,1,12,1,12,1,12,5,12,236,
        8,12,10,12,12,12,239,9,12,1,13,1,13,1,14,1,14,3,14,245,8,14,1,15,
        1,15,3,15,249,8,15,1,15,0,1,22,16,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,0,7,1,0,23,24,2,0,25,26,32,32,1,0,27,29,1,0,25,26,2,
        0,19,20,30,31,1,0,17,18,4,0,7,7,10,10,12,12,45,45,283,0,34,1,0,0,
        0,2,40,1,0,0,0,4,52,1,0,0,0,6,57,1,0,0,0,8,67,1,0,0,0,10,75,1,0,
        0,0,12,133,1,0,0,0,14,135,1,0,0,0,16,144,1,0,0,0,18,157,1,0,0,0,
        20,165,1,0,0,0,22,199,1,0,0,0,24,232,1,0,0,0,26,240,1,0,0,0,28,244,
        1,0,0,0,30,248,1,0,0,0,32,35,3,2,1,0,33,35,3,6,3,0,34,32,1,0,0,0,
        34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,38,1,
        0,0,0,38,39,5,0,0,1,39,1,1,0,0,0,40,41,5,13,0,0,41,42,5,45,0,0,42,
        46,5,35,0,0,43,45,3,4,2,0,44,43,1,0,0,0,45,48,1,0,0,0,46,44,1,0,
        0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,46,1,0,0,0,49,50,5,36,0,0,50,
        51,5,39,0,0,51,3,1,0,0,0,52,53,3,26,13,0,53,54,5,45,0,0,54,55,5,
        39,0,0,55,5,1,0,0,0,56,58,3,28,14,0,57,56,1,0,0,0,57,58,1,0,0,0,
        58,59,1,0,0,0,59,60,5,45,0,0,60,62,5,37,0,0,61,63,3,8,4,0,62,61,
        1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,65,5,38,0,0,65,66,3,14,7,
        0,66,7,1,0,0,0,67,72,3,10,5,0,68,69,5,40,0,0,69,71,3,10,5,0,70,68,
        1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,9,1,0,0,0,74,
        72,1,0,0,0,75,76,3,26,13,0,76,77,5,45,0,0,77,11,1,0,0,0,78,79,5,
        9,0,0,79,80,5,37,0,0,80,81,3,22,11,0,81,82,5,38,0,0,82,85,3,12,6,
        0,83,84,5,6,0,0,84,86,3,12,6,0,85,83,1,0,0,0,85,86,1,0,0,0,86,134,
        1,0,0,0,87,88,5,16,0,0,88,89,5,37,0,0,89,90,3,22,11,0,90,91,5,38,
        0,0,91,92,3,12,6,0,92,134,1,0,0,0,93,94,5,8,0,0,94,95,5,37,0,0,95,
        97,3,18,9,0,96,98,3,22,11,0,97,96,1,0,0,0,97,98,1,0,0,0,98,99,1,
        0,0,0,99,101,5,39,0,0,100,102,3,22,11,0,101,100,1,0,0,0,101,102,
        1,0,0,0,102,103,1,0,0,0,103,104,5,38,0,0,104,105,3,12,6,0,105,134,
        1,0,0,0,106,107,5,14,0,0,107,108,5,37,0,0,108,109,3,22,11,0,109,
        110,5,38,0,0,110,114,5,35,0,0,111,113,3,20,10,0,112,111,1,0,0,0,
        113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,0,115,117,1,0,0,0,
        116,114,1,0,0,0,117,118,5,36,0,0,118,134,1,0,0,0,119,120,5,2,0,0,
        120,134,5,39,0,0,121,122,5,4,0,0,122,134,5,39,0,0,123,125,5,11,0,
        0,124,126,3,22,11,0,125,124,1,0,0,0,125,126,1,0,0,0,126,127,1,0,
        0,0,127,134,5,39,0,0,128,134,3,14,7,0,129,134,3,16,8,0,130,131,3,
        22,11,0,131,132,5,39,0,0,132,134,1,0,0,0,133,78,1,0,0,0,133,87,1,
        0,0,0,133,93,1,0,0,0,133,106,1,0,0,0,133,119,1,0,0,0,133,121,1,0,
        0,0,133,123,1,0,0,0,133,128,1,0,0,0,133,129,1,0,0,0,133,130,1,0,
        0,0,134,13,1,0,0,0,135,139,5,35,0,0,136,138,3,12,6,0,137,136,1,0,
        0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,142,1,0,
        0,0,141,139,1,0,0,0,142,143,5,36,0,0,143,15,1,0,0,0,144,145,3,30,
        15,0,145,148,5,45,0,0,146,147,5,33,0,0,147,149,3,22,11,0,148,146,
        1,0,0,0,148,149,1,0,0,0,149,150,1,0,0,0,150,151,5,39,0,0,151,17,
        1,0,0,0,152,158,3,16,8,0,153,155,3,22,11,0,154,153,1,0,0,0,154,155,
        1,0,0,0,155,156,1,0,0,0,156,158,5,39,0,0,157,152,1,0,0,0,157,154,
        1,0,0,0,158,19,1,0,0,0,159,160,5,3,0,0,160,161,3,22,11,0,161,162,
        5,41,0,0,162,166,1,0,0,0,163,164,5,5,0,0,164,166,5,41,0,0,165,159,
        1,0,0,0,165,163,1,0,0,0,166,167,1,0,0,0,167,165,1,0,0,0,167,168,
        1,0,0,0,168,172,1,0,0,0,169,171,3,12,6,0,170,169,1,0,0,0,171,174,
        1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,21,1,0,0,0,174,172,1,
        0,0,0,175,176,6,11,-1,0,176,177,5,45,0,0,177,179,5,37,0,0,178,180,
        3,24,12,0,179,178,1,0,0,0,179,180,1,0,0,0,180,181,1,0,0,0,181,200,
        5,38,0,0,182,184,5,35,0,0,183,185,3,24,12,0,184,183,1,0,0,0,184,
        185,1,0,0,0,185,186,1,0,0,0,186,200,5,36,0,0,187,200,5,45,0,0,188,
        200,5,43,0,0,189,200,5,42,0,0,190,200,5,44,0,0,191,192,5,37,0,0,
        192,193,3,22,11,0,193,194,5,38,0,0,194,200,1,0,0,0,195,196,7,0,0,
        0,196,200,3,22,11,9,197,198,7,1,0,0,198,200,3,22,11,8,199,175,1,
        0,0,0,199,182,1,0,0,0,199,187,1,0,0,0,199,188,1,0,0,0,199,189,1,
        0,0,0,199,190,1,0,0,0,199,191,1,0,0,0,199,195,1,0,0,0,199,197,1,
        0,0,0,200,229,1,0,0,0,201,202,10,7,0,0,202,203,7,2,0,0,203,228,3,
        22,11,8,204,205,10,6,0,0,205,206,7,3,0,0,206,228,3,22,11,7,207,208,
        10,5,0,0,208,209,7,4,0,0,209,228,3,22,11,6,210,211,10,4,0,0,211,
        212,7,5,0,0,212,228,3,22,11,5,213,214,10,3,0,0,214,215,5,21,0,0,
        215,228,3,22,11,4,216,217,10,2,0,0,217,218,5,22,0,0,218,228,3,22,
        11,3,219,220,10,1,0,0,220,221,5,33,0,0,221,228,3,22,11,1,222,223,
        10,11,0,0,223,224,5,34,0,0,224,228,5,45,0,0,225,226,10,10,0,0,226,
        228,7,0,0,0,227,201,1,0,0,0,227,204,1,0,0,0,227,207,1,0,0,0,227,
        210,1,0,0,0,227,213,1,0,0,0,227,216,1,0,0,0,227,219,1,0,0,0,227,
        222,1,0,0,0,227,225,1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,
        230,1,0,0,0,230,23,1,0,0,0,231,229,1,0,0,0,232,237,3,22,11,0,233,
        234,5,40,0,0,234,236,3,22,11,0,235,233,1,0,0,0,236,239,1,0,0,0,237,
        235,1,0,0,0,237,238,1,0,0,0,238,25,1,0,0,0,239,237,1,0,0,0,240,241,
        7,6,0,0,241,27,1,0,0,0,242,245,5,15,0,0,243,245,3,26,13,0,244,242,
        1,0,0,0,244,243,1,0,0,0,245,29,1,0,0,0,246,249,5,1,0,0,247,249,3,
        26,13,0,248,246,1,0,0,0,248,247,1,0,0,0,249,31,1,0,0,0,27,34,36,
        46,57,62,72,85,97,101,114,125,133,139,148,154,157,165,167,172,179,
        184,199,227,229,237,244,248
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
            self.state = 34 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
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

                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372135040) != 0)):
                    break

            self.state = 38
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
            self.state = 40
            self.match(TyCParser.STRUCT)
            self.state = 41
            self.match(TyCParser.ID)
            self.state = 42
            self.match(TyCParser.LB)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372094080) != 0):
                self.state = 43
                self.memberDecl()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self.match(TyCParser.RB)
            self.state = 50
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
            self.state = 52
            self.explicitType()
            self.state = 53
            self.match(TyCParser.ID)
            self.state = 54
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
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 56
                self.returnType()


            self.state = 59
            self.match(TyCParser.ID)
            self.state = 60
            self.match(TyCParser.LP)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372094080) != 0):
                self.state = 61
                self.paramList()


            self.state = 64
            self.match(TyCParser.RP)
            self.state = 65
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
            self.state = 67
            self.param()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 68
                self.match(TyCParser.COMMA)
                self.state = 69
                self.param()
                self.state = 74
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
            self.state = 75
            self.explicitType()
            self.state = 76
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
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = TyCParser.IfStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.match(TyCParser.IF)
                self.state = 79
                self.match(TyCParser.LP)
                self.state = 80
                self.expr(0)
                self.state = 81
                self.match(TyCParser.RP)
                self.state = 82
                self.stmt()
                self.state = 85
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 83
                    self.match(TyCParser.ELSE)
                    self.state = 84
                    self.stmt()


                pass

            elif la_ == 2:
                localctx = TyCParser.WhileStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(TyCParser.WHILE)
                self.state = 88
                self.match(TyCParser.LP)
                self.state = 89
                self.expr(0)
                self.state = 90
                self.match(TyCParser.RP)
                self.state = 91
                self.stmt()
                pass

            elif la_ == 3:
                localctx = TyCParser.ForStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.match(TyCParser.FOR)
                self.state = 94
                self.match(TyCParser.LP)
                self.state = 95
                self.forInit()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66146917154816) != 0):
                    self.state = 96
                    self.expr(0)


                self.state = 99
                self.match(TyCParser.SEMI)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66146917154816) != 0):
                    self.state = 100
                    self.expr(0)


                self.state = 103
                self.match(TyCParser.RP)
                self.state = 104
                self.stmt()
                pass

            elif la_ == 4:
                localctx = TyCParser.SwitchStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                self.match(TyCParser.SWITCH)
                self.state = 107
                self.match(TyCParser.LP)
                self.state = 108
                self.expr(0)
                self.state = 109
                self.match(TyCParser.RP)
                self.state = 110
                self.match(TyCParser.LB)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3 or _la==5:
                    self.state = 111
                    self.switchCase()
                    self.state = 116
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 117
                self.match(TyCParser.RB)
                pass

            elif la_ == 5:
                localctx = TyCParser.BreakStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 119
                self.match(TyCParser.BREAK)
                self.state = 120
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 6:
                localctx = TyCParser.ContinueStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 121
                self.match(TyCParser.CONTINUE)
                self.state = 122
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 7:
                localctx = TyCParser.ReturnStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 123
                self.match(TyCParser.RETURN)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66146917154816) != 0):
                    self.state = 124
                    self.expr(0)


                self.state = 127
                self.match(TyCParser.SEMI)
                pass

            elif la_ == 8:
                localctx = TyCParser.BlockStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 128
                self.block()
                pass

            elif la_ == 9:
                localctx = TyCParser.VarDeclStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 129
                self.varDecl()
                pass

            elif la_ == 10:
                localctx = TyCParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 130
                self.expr(0)
                self.state = 131
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
            self.state = 135
            self.match(TyCParser.LB)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 66146917244822) != 0):
                self.state = 136
                self.stmt()
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
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
            self.state = 144
            self.varType()
            self.state = 145
            self.match(TyCParser.ID)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 146
                self.match(TyCParser.ASSIGN)
                self.state = 147
                self.expr(0)


            self.state = 150
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
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66146917154816) != 0):
                    self.state = 153
                    self.expr(0)


                self.state = 156
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
            self.state = 165 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 165
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3]:
                        self.state = 159
                        self.match(TyCParser.CASE)
                        self.state = 160
                        self.expr(0)
                        self.state = 161
                        self.match(TyCParser.COLON)
                        pass
                    elif token in [5]:
                        self.state = 163
                        self.match(TyCParser.DEFAULT)
                        self.state = 164
                        self.match(TyCParser.COLON)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 167 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 66146917244822) != 0):
                self.state = 169
                self.stmt()
                self.state = 174
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
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = TyCParser.FuncCallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 176
                self.match(TyCParser.ID)
                self.state = 177
                self.match(TyCParser.LP)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66146917154816) != 0):
                    self.state = 178
                    self.exprList()


                self.state = 181
                self.match(TyCParser.RP)
                pass

            elif la_ == 2:
                localctx = TyCParser.StructLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 182
                self.match(TyCParser.LB)
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66146917154816) != 0):
                    self.state = 183
                    self.exprList()


                self.state = 186
                self.match(TyCParser.RB)
                pass

            elif la_ == 3:
                localctx = TyCParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 187
                self.match(TyCParser.ID)
                pass

            elif la_ == 4:
                localctx = TyCParser.IntLitExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 188
                self.match(TyCParser.INTLIT)
                pass

            elif la_ == 5:
                localctx = TyCParser.FloatLitExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 189
                self.match(TyCParser.FLOATLIT)
                pass

            elif la_ == 6:
                localctx = TyCParser.StringLitExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 190
                self.match(TyCParser.STRLIT)
                pass

            elif la_ == 7:
                localctx = TyCParser.ParentExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 191
                self.match(TyCParser.LP)
                self.state = 192
                self.expr(0)
                self.state = 193
                self.match(TyCParser.RP)
                pass

            elif la_ == 8:
                localctx = TyCParser.PrefixExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 195
                _la = self._input.LA(1)
                if not(_la==23 or _la==24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 196
                self.expr(9)
                pass

            elif la_ == 9:
                localctx = TyCParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 197
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4395630592) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 198
                self.expr(8)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 227
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = TyCParser.BinaryOpContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 201
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 202
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 203
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = TyCParser.BinaryOpContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 204
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 205
                        _la = self._input.LA(1)
                        if not(_la==25 or _la==26):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 206
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = TyCParser.BinaryOpContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 207
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 208
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3222798336) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 209
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = TyCParser.BinaryOpContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 210
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 211
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 212
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = TyCParser.BinaryOpContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 213
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 214
                        self.match(TyCParser.AND)
                        self.state = 215
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = TyCParser.BinaryOpContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 216
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 217
                        self.match(TyCParser.OR)
                        self.state = 218
                        self.expr(3)
                        pass

                    elif la_ == 7:
                        localctx = TyCParser.AssignExprContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 219
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 220
                        self.match(TyCParser.ASSIGN)
                        self.state = 221
                        self.expr(1)
                        pass

                    elif la_ == 8:
                        localctx = TyCParser.MemberAccessContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 222
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 223
                        self.match(TyCParser.DOT)
                        self.state = 224
                        self.match(TyCParser.ID)
                        pass

                    elif la_ == 9:
                        localctx = TyCParser.PostfixExprContext(self, TyCParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 225
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 226
                        _la = self._input.LA(1)
                        if not(_la==23 or _la==24):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        pass

             
                self.state = 231
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
            self.state = 232
            self.expr(0)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 233
                self.match(TyCParser.COMMA)
                self.state = 234
                self.expr(0)
                self.state = 239
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
            self.state = 240
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
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.match(TyCParser.VOID)
                pass
            elif token in [7, 10, 12, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
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
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(TyCParser.AUTO)
                pass
            elif token in [7, 10, 12, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
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
         




