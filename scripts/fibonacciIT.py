# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 11:25:14 2015

@author: pedrogonzalez
"""

def fibonacciIte(n):
    a, b = 0,1
    for i in range(n):
        a, b = b, a+b
    return a