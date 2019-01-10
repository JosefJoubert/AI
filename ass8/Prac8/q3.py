# -*- coding: utf-8 -*-
from math import *
import csv
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

f= lambda x:    np.tanh(x)
df = lambda x: 1-(np.tanh(x))**2
EH = []

def BackProp():
    inputdata = list(csv.reader(open('Datasets/q3TrainInputs.csv')))  
    targets = list(csv.reader(open('Datasets/q3TrainTargets.csv')))
    random.seed(1)
    h = 13
    learning = 10
    wih = [[random.random() for i in range(h)] for j in range(len(inputdata))]
    who = [[random.random() for i in range(len(targets))] for j in range(h)]
    for s in range(10):
        EHS = []
        for epoch in range(len(inputdata[0])):
            feat = []
            for t in range(len(inputdata)):
                feat.append(float(inputdata[t][epoch]))
        
            hiddens = [0.0 for i in range(h)]
            for x in range(h):
                for y in range(len(feat)):
                    hiddens[x] = hiddens[x] + feat[y]*wih[y][x]
                #hiddens[x] = f(hiddens[x])
            outs = [0.0 for i in range(len(targets))]
            for x in range(len(outs)):
                for y in range(len(hiddens)):
                    outs[x] = outs[x] + f(hiddens[y])*who[y][x]
                    #outs[x] = f(outs[x])
            J = (float(targets[0][epoch])-outs[0])**2+(float(targets[1][epoch])-outs[1])**2+(float(targets[2][epoch])-outs[2])**2
            J = J/3
            EHS.append(J)
            errors = []
            dz = []
            for x in range(len(outs)):
                errors.append(f(outs[x])-float(targets[x][epoch]))
                dz.append(errors[x]*df(outs[x]))
            dy = []
            for x in range(len(hiddens)):
                err = 0
                for y in range(len(targets)):
                    err = err + who[x][y]*dz[y]
                dy.append(err*df(hiddens[x]))
            for x in range(len(outs)):
                for y in range(len(hiddens)):
                    who[y][x] = who[y][x] + hiddens[y]*learning*dz[x]
            for x in range(len(feat)):
                for y in range(len(hiddens)):
                    wih[x][y] = wih[x][y] + feat[x]*learning*dy[y]
        EH.append(np.average(EHS))
    print EH
    
    
BackProp()