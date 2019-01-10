# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:17:14 2016

@author: kameelperd64
"""
import numpy as np
import matplotlib.pyplot as plt
import math

c = 3*math.pow(10,8)
f = 2.5*math.pow(10,6)
d = np.arange(0.0,40,0.1)
epsilon = math.sqrt(2.25)
lamda = c/(f*epsilon)
j = complex(0,1)
beta = 2*math.pi/lamda
print beta
vsc = 2*j*np.sin(beta*d)
voc = 2*np.cos(beta*d)
plt.plot(d,np.imag(vsc))
plt.show

