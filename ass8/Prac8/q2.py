from math import *
import csv
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

#Define the sigmoid functions
#f= lambda x:    1/(1+exp(-float(x)))
f= lambda x:    np.tanh(x)
df = lambda x: 1-(np.tanh(x))**2
        

def BackProp(data,targets):
    global w1
    global w2
    learning = 0.05
    Errors = []
    random.seed(1)
    w1 = [[2*random.random()-1 for i in range(2)] for j in range(3)]
    w2 = [2-random.random()-1 for i in range(3)]
    x3 = 1
    for x in range(100):
        Errors = []
        for epoch in range(720):
            
            x1 = data[0][epoch]
            x2 = data[1][epoch]
            y1 = f(x1*w1[0][0]+x2*w1[1][0]+x3*w1[2][0])
            y2 = f(x1*w1[0][1]+x2*w1[1][1]+x3*w1[2][1])
            z1 = f(y1*w2[0]+y2*w2[1]+w2[2])

            J = (float(targets[0][epoch])-z1)**2
            
            Errors.append(J)
            dz = (float(targets[0][epoch])-z1)*df(y1*w2[0]+y2*w2[1]+w2[2])
            dy1 = dz*w2[0]*df(x1*w1[0][0]+x2*w1[1][0]+x3*w1[2][0])
            dy2 = dz*w2[1]*df(x1*w1[0][1]+x2*w1[1][1]+x3*w1[2][1])
            w2[0] = w2[0] + learning*y1*dz
            w2[1] = w2[1] + learning*y2*dz
            w2[2] = w2[2] + learning*1*dz
            w1[0][0] = w1[0][0] + learning*x1*dy1
            w1[0][1] = w1[0][1] + learning*x1*dy2
            w1[1][0] = w1[1][0] + learning*x2*dy1
            w1[1][1] = w1[1][1] + learning*x2*dy2
            w1[2][0] = w1[2][0] + learning*1*dy1
            w1[2][1] = w1[2][1] + learning*1*dy2
        #print np.average(Errors)


def ffNeuralNet(inputs):
    global w1
    global w2
    x1 = inputs[0]
    x2 = inputs[1]
    x3 = 0
    y1 = f(x1*w1[0][0]+x2*w1[1][0]+x3*w1[2][0])
    y2 = f(x1*w1[0][1]+x2*w1[1][1]+x3*w1[2][1])
    z1 = f(y1*w2[0]+y2*w2[1]+w2[2])
    return z1

global w1
global w2    
inputdata = list(csv.reader(open('q2inputs.csv')))  
targets = list(csv.reader(open('q2targets.csv')))
for x in range(len(inputdata)):
    for y in range(len(inputdata[0])):
        inputdata[x][y] = f(float(inputdata[x][y]))

BackProp(inputdata,targets)
data = [[float(0) for i in range(16)] for j in range(16)]
for x in range(16):
    for y in range(16):
        data[x][y] = ffNeuralNet([x,y])
i = 0
j = 0
Z = np.zeros((21,21))
for x1 in np.arange(0,1,0.05):
    i = 0
    for x2 in np.arange(0,1,0.05):
        Z[i,j] = ffNeuralNet([x1*20,x2*20])
        i = i+1
    j = j+1
X = np. arange (0 , 21 , 1)
Y = np. arange (0 , 21 , 1) 
X, Y = np. meshgrid(X, Y)
fig = plt . figure ()
ax = fig . gca( projection='3d' )
surf = ax.plot_surface(X, Y, Z,rstride =1,cstride =1,cmap=cm.coolwarm)
ax.set_zlim(0,1)






