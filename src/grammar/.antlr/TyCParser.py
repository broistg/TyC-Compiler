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
        4,1,52,106,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        4,0,29,8,0,11,0,12,0,30,1,0,1,0,1,1,1,1,1,1,1,1,5,1,39,8,1,10,1,
        12,1,42,9,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,3,3,52,8,3,1,3,1,3,1,
        3,3,3,57,8,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,65,8,4,10,4,12,4,68,9,4,
        1,5,1,5,1,5,1,6,1,6,5,6,75,8,6,10,6,12,6,78,9,6,1,6,1,6,1,7,1,7,
        3,7,84,8,7,1,8,1,8,1,8,1,8,3,8,90,8,8,1,8,1,8,1,9,1,9,1,10,1,10,
        1,11,1,11,3,11,100,8,11,1,12,1,12,3,12,104,8,12,1,12,0,0,13,0,2,
        4,6,8,10,12,14,16,18,20,22,24,0,1,4,0,8,8,11,11,13,13,46,46,103,
        0,28,1,0,0,0,2,34,1,0,0,0,4,46,1,0,0,0,6,51,1,0,0,0,8,61,1,0,0,0,
        10,69,1,0,0,0,12,72,1,0,0,0,14,83,1,0,0,0,16,85,1,0,0,0,18,93,1,
        0,0,0,20,95,1,0,0,0,22,99,1,0,0,0,24,103,1,0,0,0,26,29,3,2,1,0,27,
        29,3,6,3,0,28,26,1,0,0,0,28,27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,
        0,30,31,1,0,0,0,31,32,1,0,0,0,32,33,5,0,0,1,33,1,1,0,0,0,34,35,5,
        14,0,0,35,36,5,46,0,0,36,40,5,36,0,0,37,39,3,4,2,0,38,37,1,0,0,0,
        39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,40,1,
        0,0,0,43,44,5,37,0,0,44,45,5,40,0,0,45,3,1,0,0,0,46,47,3,20,10,0,
        47,48,5,46,0,0,48,49,5,40,0,0,49,5,1,0,0,0,50,52,3,22,11,0,51,50,
        1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,54,5,46,0,0,54,56,5,38,0,
        0,55,57,3,8,4,0,56,55,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,59,
        5,39,0,0,59,60,3,12,6,0,60,7,1,0,0,0,61,66,3,10,5,0,62,63,5,41,0,
        0,63,65,3,10,5,0,64,62,1,0,0,0,65,68,1,0,0,0,66,64,1,0,0,0,66,67,
        1,0,0,0,67,9,1,0,0,0,68,66,1,0,0,0,69,70,3,20,10,0,70,71,5,46,0,
        0,71,11,1,0,0,0,72,76,5,36,0,0,73,75,3,14,7,0,74,73,1,0,0,0,75,78,
        1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,
        79,80,5,37,0,0,80,13,1,0,0,0,81,84,3,16,8,0,82,84,3,12,6,0,83,81,
        1,0,0,0,83,82,1,0,0,0,84,15,1,0,0,0,85,86,3,24,12,0,86,89,5,46,0,
        0,87,88,5,34,0,0,88,90,3,18,9,0,89,87,1,0,0,0,89,90,1,0,0,0,90,91,
        1,0,0,0,91,92,5,40,0,0,92,17,1,0,0,0,93,94,5,1,0,0,94,19,1,0,0,0,
        95,96,7,0,0,0,96,21,1,0,0,0,97,100,5,16,0,0,98,100,3,20,10,0,99,
        97,1,0,0,0,99,98,1,0,0,0,100,23,1,0,0,0,101,104,5,2,0,0,102,104,
        3,20,10,0,103,101,1,0,0,0,103,102,1,0,0,0,104,25,1,0,0,0,11,28,30,
        40,51,56,66,76,83,89,99,103
    ]

class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'expr'", "'auto'", "'break'", "'case'", 
                     "'continue'", "'default'", "'else'", "'float'", "'for'", 
                     "'if'", "'int'", "'return'", "'string'", "'struct'", 
                     "'switch'", "'void'", "'while'", "'=='", "'!='", "'<='", 
                     "'>='", "'&&'", "'||'", "'++'", "'--'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'<'", "'>'", "'!'", "'='", "'.'", 
                     "'{'", "'}'", "'('", "')'", "';'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "AUTO", "BREAK", "CASE", 
                      "CONTINUE", "DEFAULT", "ELSE", "FLOAT", "FOR", "IF", 
                      "INT", "RETURN", "STRING", "STRUCT", "SWITCH", "VOID", 
                      "WHILE", "EQ", "NEQ", "LEQ", "GEQ", "AND", "OR", "INCR", 
                      "DECR", "ADD", "SUB", "MUL", "DIV", "MOD", "LT", "GT", 
                      "NOT", "ASSIGN", "DOT", "LB", "RB", "LP", "RP", "SEMI", 
                      "COMMA", "COLON", "FLOATLIT", "INTLIT", "STRLIT", 
                      "ID", "BLOCK_COMMENT", "LINE_COMMENT", "WS", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_structDecl = 1
    RULE_memberDecl = 2
    RULE_funcDecl = 3
    RULE_paramList = 4
    RULE_param = 5
    RULE_block = 6
    RULE_stmt = 7
    RULE_varDecl = 8
    RULE_expr = 9
    RULE_explicitType = 10
    RULE_returnType = 11
    RULE_varType = 12

    ruleNames =  [ "program", "structDecl", "memberDecl", "funcDecl", "paramList", 
                   "param", "block", "stmt", "varDecl", "expr", "explicitType", 
                   "returnType", "varType" ]

    EOF = Token.EOF
    T__0=1
    AUTO=2
    BREAK=3
    CASE=4
    CONTINUE=5
    DEFAULT=6
    ELSE=7
    FLOAT=8
    FOR=9
    IF=10
    INT=11
    RETURN=12
    STRING=13
    STRUCT=14
    SWITCH=15
    VOID=16
    WHILE=17
    EQ=18
    NEQ=19
    LEQ=20
    GEQ=21
    AND=22
    OR=23
    INCR=24
    DECR=25
    ADD=26
    SUB=27
    MUL=28
    DIV=29
    MOD=30
    LT=31
    GT=32
    NOT=33
    ASSIGN=34
    DOT=35
    LB=36
    RB=37
    LP=38
    RP=39
    SEMI=40
    COMMA=41
    COLON=42
    FLOATLIT=43
    INTLIT=44
    STRLIT=45
    ID=46
    BLOCK_COMMENT=47
    LINE_COMMENT=48
    WS=49
    ILLEGAL_ESCAPE=50
    UNCLOSE_STRING=51
    ERROR_CHAR=52

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
            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [14]:
                    self.state = 26
                    self.structDecl()
                    pass
                elif token in [8, 11, 13, 16, 46]:
                    self.state = 27
                    self.funcDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 70368744270080) != 0)):
                    break

            self.state = 32
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
            self.state = 34
            self.match(TyCParser.STRUCT)
            self.state = 35
            self.match(TyCParser.ID)
            self.state = 36
            self.match(TyCParser.LB)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70368744188160) != 0):
                self.state = 37
                self.memberDecl()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.match(TyCParser.RB)
            self.state = 44
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
            self.state = 46
            self.explicitType()
            self.state = 47
            self.match(TyCParser.ID)
            self.state = 48
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
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 50
                self.returnType()


            self.state = 53
            self.match(TyCParser.ID)
            self.state = 54
            self.match(TyCParser.LP)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 70368744188160) != 0):
                self.state = 55
                self.paramList()


            self.state = 58
            self.match(TyCParser.RP)
            self.state = 59
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
            self.state = 61
            self.param()
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 62
                self.match(TyCParser.COMMA)
                self.state = 63
                self.param()
                self.state = 68
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
            self.state = 69
            self.explicitType()
            self.state = 70
            self.match(TyCParser.ID)
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
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(TyCParser.LB)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70437463664900) != 0):
                self.state = 73
                self.stmt()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self.match(TyCParser.RB)
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

        def varDecl(self):
            return self.getTypedRuleContext(TyCParser.VarDeclContext,0)


        def block(self):
            return self.getTypedRuleContext(TyCParser.BlockContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_stmt




    def stmt(self):

        localctx = TyCParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stmt)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 8, 11, 13, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.varDecl()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.block()
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
            self.state = 85
            self.varType()
            self.state = 86
            self.match(TyCParser.ID)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 87
                self.match(TyCParser.ASSIGN)
                self.state = 88
                self.expr()


            self.state = 91
            self.match(TyCParser.SEMI)
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




    def expr(self):

        localctx = TyCParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(TyCParser.T__0)
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
        self.enterRule(localctx, 20, self.RULE_explicitType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 70368744188160) != 0)):
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
        self.enterRule(localctx, 22, self.RULE_returnType)
        try:
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.match(TyCParser.VOID)
                pass
            elif token in [8, 11, 13, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 98
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
        self.enterRule(localctx, 24, self.RULE_varType)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(TyCParser.AUTO)
                pass
            elif token in [8, 11, 13, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
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





