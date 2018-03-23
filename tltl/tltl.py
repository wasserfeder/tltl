'''
 Copyright (C) 2015-2016 Cristian Ioan Vasile <cvasile@bu.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 See license.txt file for license information.
'''

# import itertools as it

import numpy as np
from antlr4 import InputStream, CommonTokenStream

from tltlLexer import tltlLexer
from tltlParser import tltlParser
from tltlVisitor import tltlVisitor


class Operation(object):
    NOP, NOT, OR, AND, IMPLIES, UNTIL, THEN, EVENT, ALWAYS, NEXT, PRED, BOOL, AP = range(13)
    opnames = [None, '!', '||', '&&', '=>', 'U', 'T', 'F', 'G', 'X', 'predicate', 'bool', 'ap']
    opcodes = {'!': NOT, '&&': AND, '||' : OR, '=>': IMPLIES,
               'T': THEN, 'U': UNTIL, 'F': EVENT, 'G': ALWAYS, 'X': NEXT}
    negop = (NOP, NOP, AND, OR, AND, NOP, NOP, ALWAYS, EVENT, NEXT, PRED, BOOL, AP)

    @classmethod
    def getCode(cls, text):
        ''' Gets the code corresponding to the string representation.
        @param text string representation of an operation
        @return the operation code of this operation
        '''
        return cls.opcodes.get(text, cls.NOP)

    @classmethod
    def getString(cls, op):
        '''Gets custom string representation for each operation.
        @param op the operation code of an operation
        @return string representation of this operation
        '''
        return cls.opnames[op]


class RelOperation(object):
    NOP, LT, LE, GT, GE, EQ, NQ = range(7)
    opnames = [None, '<', '<=', '>', '>=', '=', '!=']
    opcodes = {'<': LT, '<=': LE, '>' : GT, '>=': GE, '=': EQ, '!=': NQ}
    negop = (NOP, GE, GT, LE, LT, NQ, EQ)

    @classmethod
    def getCode(cls, text):
        return cls.opcodes.get(text, cls.NOP)

    @classmethod
    def getString(cls, rop):
        return cls.opnames[rop]


class TLTLFormula(object):
    ''' TODO:
    '''
    maximumRobustness = float('inf')

    def __init__(self, operation, **kwargs):
        '''TODO:
        '''
        self.op = operation

        if self.op == Operation.BOOL:
            self.value = kwargs['value']
        elif self.op == Operation.AP:
            self.name = kwargs['ap']
        elif self.op == Operation.PRED:
            self.relation = kwargs['relation']
            self.variable = kwargs['variable']
            self.threshold = kwargs['threshold']
        elif self.op in (Operation.AND, Operation.OR, Operation.IMPLIES):
            self.left = kwargs['left']
            self.right = kwargs['right']
        elif self.op == Operation.NOT:
            self.child = kwargs['child']
        elif self.op in(Operation.ALWAYS, Operation.EVENT, Operation.NEXT):
            self.child = kwargs['child']
        elif self.op in (Operation.UNTIL, Operation.THEN):
            self.left = kwargs['left']
            self.right = kwargs['right']

    def robustness(self, s, t1, t2):
        '''TODO:
        '''
        if self.op == Operation.BOOL:
            return self.maximumRobustness
        elif self.op == Operation.PRED:
            value = s.value(self.variable, t1)
            if self.relation in (RelOperation.GE, RelOperation.GT):
                return  value - self.threshold
            elif self.relation in (RelOperation.LE, RelOperation.LT):
                return self.threshold - value
            elif self.relation == RelOperation.EQ:
                return -abs(value - self.threshold)
            elif self.relation == RelOperation.NE:
                return abs(value - self.threshold)
            else:
                raise ValueError('Unknown comparison relation code!')
        elif self.op == Operation.AND:
            return min(self.left.robustness(s, t1, t2), self.right.robustness(s, t1, t2))
        elif self.op == Operation.OR:
            return max(self.left.robustness(s, t1, t2), self.right.robustness(s, t1, t2))
        elif self.op == Operation.IMPLIES:
            return max(-self.left.robustness(s, t1, t2), self.right.robustness(s, t1, t2))
        elif self.op == Operation.NOT:
            return -self.child.robustness(s, t1, t2)
        else:
            assert t1 < t2  # has to be a temporal operator after this point
                            # all boolean operators must come before this point
        if self.op == Operation.UNTIL:
            r_max = -self.maximumRobustness
            for t_p in range(t1, t2):
                r2 = self.right.robusness(s, t_p, t2) # robustness of rhs
                r1_acc = min( (self.left.robustness(s, t_pp, t_p+1) # robustness of lhs  #TODO: CHECK THIS
                                                    for t_pp in range(t1, t_p+1)))  #TODO: CHECK THIS
                r = min(r2, r1_acc) # inside of max operator
                r_max = max(r, r_max)
            return r_max
        elif self.op == Operation.THEN:
            r_max = -self.maximumRobustness
            for t_p in range(t1, t2):
                r2 = self.right.robustness(s, t_p, t2) # robustness of rhs
                r1_acc = max( (self.left.robustness(s, t_pp, t_p+1) # robustness of lhs #TODO: CHECK THIS
                                                    for t_pp in range(t1, t_p+1)))  #TODO: CHECK THIS
                r = min(r2, r1_acc) # inside of max operator
                r_max = max(r, r_max)
            return r_max
        elif self.op == Operation.ALWAYS:
            return min( (self.child.robustness(s, tau, t2)
                                                    for tau in range(t1, t2)))
        elif self.op == Operation.EVENT:
            return max( (self.child.robustness(s, tau, t2)
                                                    for tau in range(t1, t2)))
        elif self.op == Operation.NEXT:
            return self.child.robustness(s, t1+1, t2)

    def to_ltl(self):
        '''TODO:
        '''

        if self.op in (Operation.PRED, Operation.BOOL, Operation.AP):
            return self
        elif self.op == Operation.THEN:
            phi1 = self.left.to_ltl()
            phi2 = self.right.to_ltl()
            XF_phi2 = TLTLFormula(Operation.NEXT,
                                child=TLTLFormula(Operation.EVENT, child=phi2))
            return TLTLFormula(Operation.EVENT,
                               child=TLTLFormula(Operation.AND, left=phi1,
                                                 right=XF_phi2))
        elif self.op in (Operation.AND, Operation.OR, Operation.IMPLIES,
                         Operation.UNTIL):
            phi_l = self.left.to_ltl()
            phi_r = self.right.to_ltl()
            return TLTLFormula(self.op, left=phi_l, right=phi_r)
        elif self.op in (Operation.NOT, Operation.ALWAYS, Operation.EVENT,
                         Operation.NEXT):
            phi_ch = self.child.to_ltl()
            return TLTLFormula(self.op, child=phi_ch)
        else:
            raise ValueError('Unknown operation code!')

#     def negate(self):
#         '''TODO:
#         '''
#         if self.op == Operation.PRED:
#             self.relation = RelOperation.negop[self.relation]
#         elif self.op in (Operation.AND, Operation.OR, Operation.IMPLIES):
#             self.left = self.left.negate()
#             self.right = self.right.negate()
#         elif self.op == Operation.NOT:
#             return self.child
#         elif self.op == Operation.UNTIL:
#             raise NotImplementedError
#         elif self.op in (Operation.ALWAYS, Operation.EVENT):
#             self.child = self.child.negate()
#         self.op = Operation.negop[self.op]
#         return self

#     def pnf(self):
#         '''TODO:
#         '''
#         if self.op == Operation.PRED:
#             pass
#         elif self.op in (Operation.AND, Operation.OR):
#             self.left = self.left.pnf()
#             self.right = self.right.pnf()
#         elif self.op == Operation.IMPLIES:
#             self.left = self.left.negate()
#             self.right = self.right.pnf()
#             self.op = Operation.OR
#         elif self.op == Operation.NOT:
#             return self.child.negate()
#         elif self.op == Operation.UNTIL:
#             raise NotImplementedError
#         elif self.op in (Operation.ALWAYS, Operation.EVENT):
#             self.child = self.child.pnf()
#         return self

    def variables(self):
        '''TODO:
        '''
        if self.op == Operation.PRED:
            return {self.variable}
        elif self.op in (Operation.AND, Operation.OR, Operation.IMPLIES,
                         Operation.UNTIL, Operation.THEN):
            return self.left.variables() | self.right.variables()
        elif self.op in (Operation.NOT, Operation.ALWAYS, Operation.EVENT,
                         Operation.NEXT):
            return self.child.variables()
        else:
            return {}

    def __eq__(self, other):
        #TODO:
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        opname = Operation.getString(self.op)
        if self.op == Operation.BOOL:
            return str(self.value)
        elif self.op == Operation.AP:
            return self.name
        elif self.op == Operation.PRED:
            return '({v} {rel} {th})'.format(v=self.variable, th=self.threshold,
                                    rel=RelOperation.getString(self.relation))
        elif self.op in (Operation.AND, Operation.OR, Operation.IMPLIES,
                       Operation.UNTIL, Operation.THEN):
            return '({left} {op} {right})'.format(left=self.left, op=opname,
                                                right=self.right)
        elif self.op in (Operation.NOT, Operation.ALWAYS, Operation.EVENT,
                         Operation.NEXT):
            return '({op} {child})'.format(op=opname, child=self.child)
        return ''


class TLTLAbstractSyntaxTreeExtractor(tltlVisitor):

    def visitFormula(self, ctx):
        op = Operation.getCode(ctx.op.text)
        ret = None

        if op in (Operation.AND, Operation.OR, Operation.IMPLIES,
                  Operation.UNTIL, Operation.THEN):
            ret = TLTLFormula(op, left=self.visit(ctx.left),
                             right=self.visit(ctx.right))
        elif op in (Operation.NOT, Operation.ALWAYS, Operation.EVENT,
                    Operation.NEXT):
            ret = TLTLFormula(op, child=self.visit(ctx.child))
        else:
            print('Error: unknown operation!')
        return ret

    def visitBooleanPred(self, ctx):
#         print 'BooleanPred'
        return self.visit(ctx.booleanExpr())

    def visitBooleanExpr(self, ctx):
#         print "BEXPR", ctx.op.text, ctx.left.getText(), ctx.right.getText()
        if ctx.op.text in ('true', 'false'): # Boolean constant
            return TLTLFormula(Operation.BOOL, value=bool(ctx.op.text))
        elif ctx.op.text not in RelOperation.opnames: # AP
            return TLTLFormula(Operation.AP, ap=ctx.op.text)
        # else: # Predicate
        return TLTLFormula(Operation.PRED, 
            relation=RelOperation.getCode(ctx.op.text),
            variable=ctx.left.getText(), threshold=float(ctx.right.getText()))

    def visitParprop(self, ctx):
        return self.visit(ctx.child);


class Trace(object):
    '''TODO:
    '''

    def __init__(self, variables, data):
        '''TODO:
        '''
        self.variables = variables
        self.data = np.array(data)

    def value(self, variable, t):
        '''TODO:
        '''
        var_idx = self.variables.index(variable)
        return self.data[var_idx][t]

    def values(self, variable):
        '''TODO:
        '''
        var_idx = self.variables.index(variable)
        return self.data[var_idx]

    def __len__(self):
        return len(data[0])

    def __str__(self):
#         String trace = "((\"time\"";
#         for (String variable : variables) {
#             trace += ", \"" + variable + "\"";
#         }
#         trace += ")";
#         for (int i = 0; i < timePoints.length; i++) {
#             trace += ",(" + timePoints[i];
#             for (double value : data[i]) {
#                 trace += ", " + value;
#             }
#             trace += ")";
#         }
#         trace += ")";
#         return trace;
        raise NotImplementedError

if __name__ == '__main__':
    lexer = tltlLexer(InputStream("!(x < 10) && F y > 2 || G z<=8 && (y < 1 T x >= 3)"))
    tokens = CommonTokenStream(lexer)

    parser = tltlParser(tokens)
    t = parser.tltlProperty()
#     print t.toStringTree()

    ast = TLTLAbstractSyntaxTreeExtractor().visit(t)
    print 'AST:', ast
    print ast.variables()
    print 'LTL', ast.to_ltl()

    varnames = ['x', 'y', 'z']
    data = [[8, 8, 11, 11, 11], [2, 3, 1, 2, 2], [3, 9, 8, 9, 9]]
    s = Trace(varnames, data)

    print 'r:', ast.robustness(s, 0, len(s))
