# -*- coding: utf-8 -*-
"""
Created on Tue May 31 18:33:53 2016

@author: kameelperd64
"""

from numpy import *
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def sigmoid(x):
    y = 1/(1+exp(-x))
    return y


f = open('examX.data')
X = []
word = f.readline().strip().split(',')
while(word[0] != ''):
    X.append([float(word[0]),float(word[1])])
    word = f.readline().strip().split(',')

f.close()
f = open('examY.data')
Y = []
word = f.readline().strip()
while (word != ''):
    Y.append(float(word))
    word = f.readline().strip()
N = len(X)
for x in range(len(X)):
    X[x].append(1)

random.seed(1)
w = [random.random(),random.random(),random.random()]
learning = 0.005
J = 2
while (J > 1):
    outputs = []
    #print w[0],w[1],w[2]
    for x in range(len(X)):
        out = X[x][0]*w[0] + X[x][1]*w[1] + X[x][2]*w[2]
        #print X[x][0],X[x][1]
        #print out
        outputs.append(sigmoid(out))
        #print sigmoid(out)
    #print outputs
    dL1 = 0
    dL2 = 0
    dL3 = 0
    J = 0
    for x in range(len(X)):
        err = Y[x]-outputs[x]
        dL1 = dL1+(X[x][0]*err) 
        dL2 = dL2+(X[x][1]*err)
        dL3 = dL3+(X[x][2]*err)
        if (err > 0.5 or err < -0.5):
            J = J+1
    dL1 = dL1/len(X)
    dL2 = dL2/len(X)
    dL3 = dL3/len(X)
    print J
    #print dL1
    #print dL2
    #print dL3
    w[0] = w[0] + learning*dL1
    w[1] = w[1] + learning*dL2
    w[2] = w[2] + learning*dL3


#y = [[0.0 for i in range(100)] for j in range(100)]
#for x in range(100):
#    for t in range(100):
#        y[x][t] = sigmoid(x*w[0] + t*w[1] + w[2])


#X = np. arange (0 , 100 , 1)
#Y = np. arange (0 , 100 , 1) 
#fig = plt.figure ()
#ax = fig.gca( projection='3d' )
#surf = ax.plot_surface(X, Y, y,rstride =1,cstride =1,cmap=cm.coolwarm)
#ax.set_zlim(0,1)
        
