# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 18:35:20 2022

@author: Mohammed Faizan
"""

class BinomialExpansion:
    """
    Describes the algebraic expansion of powers of a binomial using Pascal's triangle.

    Parameters
    ----------
    expr : str
        string in format of (x + y)**n.
        here, x and y can be any number.
        n must be a positive integer.

    Returns
    -------
    1. Expansion of the given expression
    2. Solution of the given expression for given x, y and n values

    """
    def __init__(self, expr):
        expr = expr.replace(' ', '')
        expr = expr.split('**')
        self.n = int(expr[-1])
        expr = expr[0]
        expr = expr.replace('(', '').replace(')', '')
        expr = expr.split('+')
        try:
            self.x = int(expr[0])
        except:
            self.x = 0
        try:
            self.y = int(expr[-1])
        except:
            self.y = 0
            
        self.list_calculated = False
        self.Expression_calculated = False
        self.solved = False
    
    def get_n_list(self):
        if not self.list_calculated:
            print('getting n list')
            self.Tri = [  [1],
                  [1, 2, 1]
                  ]
            for i in range(1, self.n-1):
                temp = [1]
                for j in range(1, len(self.Tri[i])):
                    a = self.Tri[i][j - 1]
                    b = self.Tri[i][j]
                    temp.append(a+b)
                self.Tri.append(temp + [1])
            self.n_list = self.Tri[-1]
            self.list_calculated = True

        return self.n_list
    
    
    def get_expression(self):
        if not self.list_calculated:
            self.get_n_list()
            
        if not self.Expression_calculated:
            print('getting expression')
            self.Expression = f'(x**{self.n})'
            for i, x_power, y_power in zip(self.n_list[1: -1], range(self.n - 1, 0, -1), range(1, self.n)):
                self.Expression = self.Expression + ' + ' + f" {i}*(x**{x_power})*(y**{y_power})"
            self.Expression = self.Expression + ' + ' + f'(y**{self.n})'
            self.Expression_calculated = True
            
        return self.Expression
    
    
    def solve(self):
        if not self.Expression_calculated:
            self.get_expression()
        
        if not self.solved:
            print('solving')
            x = self.x
            y = self.y
            n = self.n
            self.result = eval(self.Expression)
            self.solved = True
            
        return self.result
    
    def new_xy(self, x = None, y = None, overwrite = False):
        if (x != None) or (y != None):
            if x is None:
                x = self.x
            if y is None:
                y = self.y

            if overwrite:
                self.x = x
                self.y = y
                self.result = eval(self.Expression)
                return self.result
            else:
                return eval(self.Expression)