#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 22:39:14 2018

@author: emily
"""

from pulp import *

import numpy as np
b = np.loadtxt('/Users/emily/.spyder-py3/example.txt')
prob = LpProblem("The least core", LpMinimize)
L = LpVariable("L",cat='Continuous')
M = LpVariable("M",cat='Continuous')
R = LpVariable("R",cat= 'Continuous')
V = LpVariable("V",cat ='Continuous')
prob += V
prob += L+ M + R == b[6]
prob += L>=b[1]-V
prob += M>=b[0]-V
prob += R>=b[2]-V
prob += L+M>=b[3]-V
prob += L+R>=b[5]-V
prob += M+R>=b[4]-V
prob.solve()
for i in prob.variables():
    print(i.name, "=", i.varValue/b[6])  
for i in prob.variables():  
  print(i.name, "=", i.varValue)            #打印每个变量名字
print( "V = ", value(prob.objective))#百分比可以为