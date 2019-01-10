# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:55:38 2016

@author: kameelperd64
"""

mylist = [1,2,3]
mylist.insert(0,5)
print mylist
x = min(mylist)
print x
y = mylist.index(x)
print y
mylist.remove(x)
print mylist