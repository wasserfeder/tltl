grammar tltl;

@header {
'''
 Copyright (C) 2018 Cristian Ioan Vasile <cvasile@mit.edu>
 Hybrid and Networked Systems (HyNeSs) Group, BU Robotics Lab, Boston University
 See license.txt file for license information.
'''
}


tltlProperty:
         '(' child=tltlProperty ')' #parprop
    |    booleanExpr #booleanPred
    |    op='!' child=tltlProperty #formula
    |    op='F' child=tltlProperty #formula
    |    op='G' child=tltlProperty #formula
    |    op='X' child=tltlProperty #formula
    |    left=tltlProperty op='=>' right=tltlProperty #formula
    |    left=tltlProperty op='&&' right=tltlProperty #formula
    |    left=tltlProperty op='||' right=tltlProperty #formula
    |    left=tltlProperty op='U' right=tltlProperty #formula
    |    left=tltlProperty op='T' right=tltlProperty #formula
    ;
expr:
        ('-('|'(') expr ')'
    |   expr '^' expr
    |   ('sqrt('|'log('|'ln('|'abs('|'der('|'int(') expr ')'
    |   expr ('*'|'/') expr
    |   expr ('+'|'-') expr
    |   RATIONAL
    |   VARIABLE
    ;
booleanExpr:
         left=expr op=('<'|'<='|'='|'>='|'>') right=expr
    |    op=BOOLEAN
    |    op=VARIABLE
    ;
BOOLEAN : ('true'|'false');
VARIABLE : ([a-z]|[A-Z])([a-z]|[A-Z]|[0-9]|'_')*;
RATIONAL : ('-')?[0-9]*('.')?[0-9]+('E'|'E-')?[0-9]* ;
WS : ( ' ' | '\t' | '\r' | '\n' )+ { self.skip(); };
