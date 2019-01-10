# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import random
import numpy as np

f = open('eyesightData/signdist.data')
age = []
dist = []
word = f.readline().strip().split(',')
while(word[0] != ''):
    age.append(float(word[0]))
    dist.append(float(word[1]))
    word = f.readline().strip().split(',')
    

ax = plt.subplot()
ax.scatter(age,dist)
ax.set_ylabel("Distance(m)")
ax.set_xlabel("Age")
learning = 0.0006
m = len(age)
random.seed(1)
W = [-1,dist[0]]
j = [1]
for j in j:
    for epoch in range(40000*j):
        outputs = []
        for x in range(m):
            outputs.append(age[x]*W[0] + W[1])
        J = 0
        for x in range(m):
            J = J + (outputs[x]-dist[x])**2
        J = np.sqrt(J)
        dw1 = 0
        dw2 = 0
        for x in range(m):
            dw1 = dw1 + age[x]*(dist[x]-outputs[x])
            dw2 = dw2 + dist[x]-outputs[x]
        dw1 = dw1/m
        dw2 = dw2/m
        W[0] = W[0] + learning*dw1
        W[1] = W[1] + learning*dw2
    X = np.arange(18,82,0.1)
    Y = []
    for i in range(len(X)):
        Y.append(X[i]*W[0]+W[1])
    ax.plot(X,Y)
    plt.show()

print 90*W[0]+W[1]