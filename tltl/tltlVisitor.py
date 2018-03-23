# Generated from /home/cristi/Dropbox/work/workspace_linux_precision5520/tltl/tltl/tltl.g4 by ANTLR 4.7.1
from antlr4 import *

'''
 Copyright (C) 2018 Cristian Ioan Vasile <cvasile@mit.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 See license.txt file for license information.
'''


# This class defines a complete generic visitor for a parse tree produced by tltlParser.

class tltlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by tltlParser#booleanPred.
    def visitBooleanPred(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tltlParser#formula.
    def visitFormula(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tltlParser#parprop.
    def visitParprop(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tltlParser#expr.
    def visitExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tltlParser#booleanExpr.
    def visitBooleanExpr(self, ctx):
        return self.visitChildren(ctx)


