# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 16:20:54 2016

@author: kameelperd64
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import random



def distance(x1,y1,x2,y2):
    if y1 < 8:
        if y2 < 8:
            return math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
        dist1 = math.sqrt(math.pow(x1-3,2)+math.pow(y1-8,2)) + math.sqrt(math.pow(3-x2,2)+math.pow(9-y2,2)) + 1
        dist2 = math.sqrt(math.pow(x1-10,2)+math.pow(y1-8,2)) + math.sqrt(math.pow(10-x2,2)+math.pow(9-y2,2)) + 1
        if dist1 < dist2:
            return dist1
        return dist2
    if y2 > 8:
        return math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
    dist1 = math.sqrt(math.pow(x1-3,2)+math.pow(y1-8,2)) + math.sqrt(math.pow(3-x2,2)+math.pow(9-y2,2)) + 1
    dist2 = math.sqrt(math.pow(x1-10,2)+math.pow(y1-8,2)) + math.sqrt(math.pow(10-x2,2)+math.pow(9-y2,2)) + 1
    if dist1 < dist2:
        return dist1
    return dist2

def costFunc(x1,y1):
    global arrWeights
    cost = 0
    for x in range (1,17):
        for y in range (1,17):
            cost = cost + arrWeights[x-1,y-1]*distance(x,y,x1,y1)
    return cost
        
def GA(oldlow):
    global popx
    global popy
    global changed
    global low
    global count
    count = count +1
    print count    
    if len(popx) == 1:
        return
    
    arrCosts = []
    for x in range(0,len(popx)-1):
        arrCosts.append(int(costFunc(popx[x]+1,popy[x]+1)))
    lowestpos = 0
    lowest = arrCosts[0]
    lenpopx = 5
    newpopx = []
    newpopy = []
    while len(newpopx) < lenpopx:
        for x in range(0,len(arrCosts)-1):
            if arrCosts[x] < lowest:
                lowest = arrCosts[x]
                lowestpos = x
        newpopx.append(popx[lowestpos])
        newpopy.append(popy[lowestpos])
        arrCosts.pop(lowestpos)
        popx.pop(lowestpos)
        popy.pop(lowestpos)
        lowestpos = 0
        lowest = arrCosts[0]
    if (len(newpopx) == 0):
        print newpopx
        return
    alllow = int(costFunc(newpopx[0]+1,newpopy[0]+1))
    print alllow
    if (alllow == oldlow):
        if  changed == 30:
            return
        changed = changed + 1
    else:
        changed = 0
    for x in range(0,len(newpopx)-1):
        for y in range(0,len(newpopy)-1):
            if y == x:
                continue
            newpopx.append(newpopx[y])
            newpopy.append(newpopy[x])
        if len(newpopx) > 50:
                break
    popx = newpopx
    popy = newpopy
    mutate()
    GA(alllow)
    
def mutate():
    global popy
    global popx
    x = random.randint(0,len(popx)-1)
    y = random.randint(0,3)
    if y ==0:
        popx[x] = popx[x] + 2
        if popx[x] > 15:
            popx[x] = 15
        popy[x] = popy[x] + 2
        if popy[x] > 15:
            popy[x] = 15
    if y ==1:
        popx[x] = popx[x] + 2
        if popx[x] > 15:
            pop[x] = 15
        popy[x] = popy[x] - 2
        if popy[x] < 0:
            popy[x] = 0
    if y == 2:
        popx[x] = popx[x] - 2
        if popx[x] < 0:
            popx[x] = 0
        popy[x] = popy[x] + 2
        if popy[x] > 15:
            popy[x] = 15
    if y == 3:
        popx[x] = popx[x] - 2
        if popx[x] < 0:
            popx[x] = 0
        popy[x] = popy[x] - 2
        if popy[x] < 0:
            popy[x] = 0

def plot():
    global arrCosts
    x = range(16)
    y = range(16)
    X,Y = np.meshgrid(x,y)
    fig = plt.figure()
    ax = fig.add_subplot(111,projection = '3d')
    ax.plot_surface(X,Y,arrCosts,rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0)
    plt.show

global arrWeights
arrWeights = np.array(
[[9, 7, 1, 9, 8, 8, 2, 8, 9, 9, 8, 5, 3, 6, 9, 5],
[9, 2, 4, 9, 9, 0, 3, 8, 9, 8, 5, 3, 7, 8, 4, 7],
[4, 7, 8, 9, 0, 6, 0, 3, 8, 7, 4, 4, 7, 1, 2, 7],
[2, 2, 4, 0, 1, 7, 1, 8, 7, 1, 9, 3, 0, 4, 1, 2],
[0, 9, 0, 3, 3, 8, 1, 8, 9, 7, 7, 7, 8, 2, 2, 1],
[1, 1, 2, 1, 9, 5, 9, 9, 8, 5, 2, 5, 0, 5, 4, 9],
[9, 1, 0, 7, 2, 1, 0, 5, 8, 7, 3, 6, 7, 6, 1, 2],
[4, 0, 3, 8, 0, 4, 2, 6, 3, 2, 0, 8, 6, 1, 7, 9],
[1, 0, 1, 3, 3, 6, 7, 0, 4, 4, 0, 3, 8, 3, 4, 7],
[1, 7, 7, 0, 5, 7, 0, 1, 1, 5, 8, 3, 5, 1, 1, 0],
[3, 1, 2, 6, 7, 1, 8, 1, 4, 5, 2, 1, 9, 8, 3, 8],
[1, 3, 2, 7, 7, 6, 3, 0, 1, 3, 2, 6, 6, 2, 0, 8],
[6, 9, 4, 8, 1, 2, 5, 5, 0, 9, 2, 8, 7, 9, 4, 9],
[0, 7, 4, 3, 4, 4, 5, 2, 8, 7, 4, 6, 9, 5, 5, 3],
[9, 1, 8, 0, 7, 2, 2, 5, 5, 8, 3, 8, 4, 3, 7, 6],
[6, 0, 0, 5, 6, 0, 8, 1, 7, 4, 5, 0, 8, 8, 8, 7]])
global arrCosts
arrCosts = [[0.0 for x in range(16)] for x in range(16)]
for x in range (1,17):
    for y in range (1,17):
        arrCosts[x-1][y-1] = costFunc(x,y)
plot()    

arrCosts = np.array(arrCosts)
print np.unravel_index(arrCosts.argmin(),arrCosts.shape) 
global popy
global popx
global changed
global low
global count
count = 0
low = int(arrCosts[9,8])
changed = 0
popx = [random.randint(0,15) for x in range(26)]
popy = [random.randint(0,15) for x in range(26)]
GA(0)




    
    
    
    
    
    