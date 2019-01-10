# -*- coding: utf-8 -*-
"""
Created on Tue May 31 11:27:18 2016

@author: kameelperd64
"""


x = [1,2,3]
y = [2,3,4]
w = [0.8,0.7]
z = []
for i in range(3):
    z.append(x[i]*w[0] + w[1])

dw1 = 0
for i in range(3):
    