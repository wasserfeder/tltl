# Generated from /home/cristi/Dropbox/work/workspace_linux_precision5520/tltl/tltl/tltl.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


'''
 Copyright (C) 2018 Cristian Ioan Vasile <cvasile@mit.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 See license.txt file for license information.
'''

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\"P\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write(u"\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\27\n\2\3\2\3\2\3\2")
        buf.write(u"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2")
        buf.write(u"(\n\2\f\2\16\2+\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\5\38\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\7\3C\n\3\f\3\16\3F\13\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\5\4N\n\4\3\4\2\4\2\4\5\2\4\6\2\7\4\2\3\3\16\16\3\2\20")
        buf.write(u"\25\3\2\26\27\3\2\30\31\3\2\32\36\2^\2\26\3\2\2\2\4\67")
        buf.write(u"\3\2\2\2\6M\3\2\2\2\b\t\b\2\1\2\t\n\7\3\2\2\n\13\5\2")
        buf.write(u"\2\2\13\f\7\4\2\2\f\27\3\2\2\2\r\27\5\6\4\2\16\17\7\5")
        buf.write(u"\2\2\17\27\5\2\2\13\20\21\7\6\2\2\21\27\5\2\2\n\22\23")
        buf.write(u"\7\7\2\2\23\27\5\2\2\t\24\25\7\b\2\2\25\27\5\2\2\b\26")
        buf.write(u"\b\3\2\2\2\26\r\3\2\2\2\26\16\3\2\2\2\26\20\3\2\2\2\26")
        buf.write(u"\22\3\2\2\2\26\24\3\2\2\2\27)\3\2\2\2\30\31\f\7\2\2\31")
        buf.write(u"\32\7\t\2\2\32(\5\2\2\b\33\34\f\6\2\2\34\35\7\n\2\2\35")
        buf.write(u"(\5\2\2\7\36\37\f\5\2\2\37 \7\13\2\2 (\5\2\2\6!\"\f\4")
        buf.write(u"\2\2\"#\7\f\2\2#(\5\2\2\5$%\f\3\2\2%&\7\r\2\2&(\5\2\2")
        buf.write(u"\4\'\30\3\2\2\2\'\33\3\2\2\2\'\36\3\2\2\2\'!\3\2\2\2")
        buf.write(u"\'$\3\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\3\3\2\2\2")
        buf.write(u"+)\3\2\2\2,-\b\3\1\2-.\t\2\2\2./\5\4\3\2/\60\7\4\2\2")
        buf.write(u"\608\3\2\2\2\61\62\t\3\2\2\62\63\5\4\3\2\63\64\7\4\2")
        buf.write(u"\2\648\3\2\2\2\658\7!\2\2\668\7 \2\2\67,\3\2\2\2\67\61")
        buf.write(u"\3\2\2\2\67\65\3\2\2\2\67\66\3\2\2\28D\3\2\2\29:\f\b")
        buf.write(u"\2\2:;\7\17\2\2;C\5\4\3\t<=\f\6\2\2=>\t\4\2\2>C\5\4\3")
        buf.write(u"\7?@\f\5\2\2@A\t\5\2\2AC\5\4\3\6B9\3\2\2\2B<\3\2\2\2")
        buf.write(u"B?\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\5\3\2\2\2F")
        buf.write(u"D\3\2\2\2GH\5\4\3\2HI\t\6\2\2IJ\5\4\3\2JN\3\2\2\2KN\7")
        buf.write(u"\37\2\2LN\7 \2\2MG\3\2\2\2MK\3\2\2\2ML\3\2\2\2N\7\3\2")
        buf.write(u"\2\2\t\26\')\67BDM")
        return buf.getvalue()


class tltlParser ( Parser ):

    grammarFileName = "tltl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'", u"'!'", u"'F'", u"'G'", 
                     u"'X'", u"'=>'", u"'&&'", u"'||'", u"'U'", u"'T'", 
                     u"'-('", u"'^'", u"'sqrt('", u"'log('", u"'ln('", u"'abs('", 
                     u"'der('", u"'int('", u"'*'", u"'/'", u"'+'", u"'-'", 
                     u"'<'", u"'<='", u"'='", u"'>='", u"'>'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"BOOLEAN", u"VARIABLE", u"RATIONAL", 
                      u"WS" ]

    RULE_tltlProperty = 0
    RULE_expr = 1
    RULE_booleanExpr = 2

    ruleNames =  [ u"tltlProperty", u"expr", u"booleanExpr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    BOOLEAN=29
    VARIABLE=30
    RATIONAL=31
    WS=32

    def __init__(self, input, output=sys.stdout):
        super(tltlParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class TltlPropertyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(tltlParser.TltlPropertyContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tltlParser.RULE_tltlProperty

     
        def copyFrom(self, ctx):
            super(tltlParser.TltlPropertyContext, self).copyFrom(ctx)


    class BooleanPredContext(TltlPropertyContext):

        def __init__(self, parser, ctx): # actually a tltlParser.TltlPropertyContext)
            super(tltlParser.BooleanPredContext, self).__init__(parser)
            self.copyFrom(ctx)

        def booleanExpr(self):
            return self.getTypedRuleContext(tltlParser.BooleanExprContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterBooleanPred"):
                listener.enterBooleanPred(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBooleanPred"):
                listener.exitBooleanPred(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitBooleanPred"):
                return visitor.visitBooleanPred(self)
            else:
                return visitor.visitChildren(self)


    class FormulaContext(TltlPropertyContext):

        def __init__(self, parser, ctx): # actually a tltlParser.TltlPropertyContext)
            super(tltlParser.FormulaContext, self).__init__(parser)
            self.left = None # TltlPropertyContext
            self.op = None # Token
            self.child = None # TltlPropertyContext
            self.right = None # TltlPropertyContext
            self.copyFrom(ctx)

        def tltlProperty(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(tltlParser.TltlPropertyContext)
            else:
                return self.getTypedRuleContext(tltlParser.TltlPropertyContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterFormula"):
                listener.enterFormula(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFormula"):
                listener.exitFormula(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitFormula"):
                return visitor.visitFormula(self)
            else:
                return visitor.visitChildren(self)


    class ParpropContext(TltlPropertyContext):

        def __init__(self, parser, ctx): # actually a tltlParser.TltlPropertyContext)
            super(tltlParser.ParpropContext, self).__init__(parser)
            self.child = None # TltlPropertyContext
            self.copyFrom(ctx)

        def tltlProperty(self):
            return self.getTypedRuleContext(tltlParser.TltlPropertyContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterParprop"):
                listener.enterParprop(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParprop"):
                listener.exitParprop(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitParprop"):
                return visitor.visitParprop(self)
            else:
                return visitor.visitChildren(self)



    def tltlProperty(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tltlParser.TltlPropertyContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_tltlProperty, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = tltlParser.ParpropContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 7
                self.match(tltlParser.T__0)
                self.state = 8
                localctx.child = self.tltlProperty(0)
                self.state = 9
                self.match(tltlParser.T__1)
                pass

            elif la_ == 2:
                localctx = tltlParser.BooleanPredContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.booleanExpr()
                pass

            elif la_ == 3:
                localctx = tltlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                localctx.op = self.match(tltlParser.T__2)
                self.state = 13
                localctx.child = self.tltlProperty(9)
                pass

            elif la_ == 4:
                localctx = tltlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                localctx.op = self.match(tltlParser.T__3)
                self.state = 15
                localctx.child = self.tltlProperty(8)
                pass

            elif la_ == 5:
                localctx = tltlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                localctx.op = self.match(tltlParser.T__4)
                self.state = 17
                localctx.child = self.tltlProperty(7)
                pass

            elif la_ == 6:
                localctx = tltlParser.FormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                localctx.op = self.match(tltlParser.T__5)
                self.state = 19
                localctx.child = self.tltlProperty(6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = tltlParser.FormulaContext(self, tltlParser.TltlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_tltlProperty)
                        self.state = 22
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 23
                        localctx.op = self.match(tltlParser.T__6)
                        self.state = 24
                        localctx.right = self.tltlProperty(6)
                        pass

                    elif la_ == 2:
                        localctx = tltlParser.FormulaContext(self, tltlParser.TltlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_tltlProperty)
                        self.state = 25
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 26
                        localctx.op = self.match(tltlParser.T__7)
                        self.state = 27
                        localctx.right = self.tltlProperty(5)
                        pass

                    elif la_ == 3:
                        localctx = tltlParser.FormulaContext(self, tltlParser.TltlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_tltlProperty)
                        self.state = 28
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 29
                        localctx.op = self.match(tltlParser.T__8)
                        self.state = 30
                        localctx.right = self.tltlProperty(4)
                        pass

                    elif la_ == 4:
                        localctx = tltlParser.FormulaContext(self, tltlParser.TltlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_tltlProperty)
                        self.state = 31
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 32
                        localctx.op = self.match(tltlParser.T__9)
                        self.state = 33
                        localctx.right = self.tltlProperty(3)
                        pass

                    elif la_ == 5:
                        localctx = tltlParser.FormulaContext(self, tltlParser.TltlPropertyContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_tltlProperty)
                        self.state = 34
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 35
                        localctx.op = self.match(tltlParser.T__10)
                        self.state = 36
                        localctx.right = self.tltlProperty(2)
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(tltlParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(tltlParser.ExprContext)
            else:
                return self.getTypedRuleContext(tltlParser.ExprContext,i)


        def RATIONAL(self):
            return self.getToken(tltlParser.RATIONAL, 0)

        def VARIABLE(self):
            return self.getToken(tltlParser.VARIABLE, 0)

        def getRuleIndex(self):
            return tltlParser.RULE_expr

        def enterRule(self, listener):
            if hasattr(listener, "enterExpr"):
                listener.enterExpr(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitExpr"):
                listener.exitExpr(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitExpr"):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = tltlParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [tltlParser.T__0, tltlParser.T__11]:
                self.state = 43
                _la = self._input.LA(1)
                if not(_la==tltlParser.T__0 or _la==tltlParser.T__11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(tltlParser.T__1)
                pass
            elif token in [tltlParser.T__13, tltlParser.T__14, tltlParser.T__15, tltlParser.T__16, tltlParser.T__17, tltlParser.T__18]:
                self.state = 47
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << tltlParser.T__13) | (1 << tltlParser.T__14) | (1 << tltlParser.T__15) | (1 << tltlParser.T__16) | (1 << tltlParser.T__17) | (1 << tltlParser.T__18))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 48
                self.expr(0)
                self.state = 49
                self.match(tltlParser.T__1)
                pass
            elif token in [tltlParser.RATIONAL]:
                self.state = 51
                self.match(tltlParser.RATIONAL)
                pass
            elif token in [tltlParser.VARIABLE]:
                self.state = 52
                self.match(tltlParser.VARIABLE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 64
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = tltlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 56
                        self.match(tltlParser.T__12)
                        self.state = 57
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = tltlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 59
                        _la = self._input.LA(1)
                        if not(_la==tltlParser.T__19 or _la==tltlParser.T__20):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = tltlParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 62
                        _la = self._input.LA(1)
                        if not(_la==tltlParser.T__21 or _la==tltlParser.T__22):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 63
                        self.expr(4)
                        pass

             
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class BooleanExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(tltlParser.BooleanExprContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.var = None # Token

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(tltlParser.ExprContext)
            else:
                return self.getTypedRuleContext(tltlParser.ExprContext,i)


        def BOOLEAN(self):
            return self.getToken(tltlParser.BOOLEAN, 0)

        def VARIABLE(self):
            return self.getToken(tltlParser.VARIABLE, 0)

        def getRuleIndex(self):
            return tltlParser.RULE_booleanExpr

        def enterRule(self, listener):
            if hasattr(listener, "enterBooleanExpr"):
                listener.enterBooleanExpr(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBooleanExpr"):
                listener.exitBooleanExpr(self)

        def accept(self, visitor):
            if hasattr(visitor, "visitBooleanExpr"):
                return visitor.visitBooleanExpr(self)
            else:
                return visitor.visitChildren(self)




    def booleanExpr(self):

        localctx = tltlParser.BooleanExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_booleanExpr)
        self._la = 0 # Token type
        try:
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                localctx.left = self.expr(0)
                self.state = 70
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << tltlParser.T__23) | (1 << tltlParser.T__24) | (1 << tltlParser.T__25) | (1 << tltlParser.T__26) | (1 << tltlParser.T__27))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 71
                localctx.right = self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                localctx.op = self.match(tltlParser.BOOLEAN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                localctx.var = self.match(tltlParser.VARIABLE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.tltlProperty_sempred
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def tltlProperty_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         

    def expr_sempred(self, localctx, predIndex):
            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         




