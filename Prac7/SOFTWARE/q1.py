# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import gc
import math
f = open('irisData/trainData.data','r')


def distance(word,sl,sw,pl,pw):
    global maxsl
    global maxsw
    global maxpl
    global maxpw    
    
    error1 = abs(float(word[0])-sl)**2
    error2 = abs(float(word[1]) - sw)**2
    error3 = abs(float(word[2])-pl)**2
    error4 = abs(float(word[3])-pw)**2
    return math.sqrt(error1+error2+error3+error4)

word = f.readline().strip().split(',')
sepallength = []
sepalwidth = []
petallength = []
petalwidth = []
while (word[0] != ''):
    sepallength.append(float(word[0]))
    sepalwidth.append(float(word[1]))
    petallength.append(float(word[2]))
    petalwidth.append(float(word[3]))
    word = f.readline().strip().split(',')

global maxsl
global maxsw
global maxpl
global maxpw
maxsl = max(sepallength)
maxsw = max(sepalwidth)
maxpl = max(petallength)
maxpw = max(petalwidth)


f = open('irisData/trainLabels.data')
labels = []
word = f.readline().strip()
while(word != ''):
    labels.append(int(word))
    word = f.readline().strip()

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
for x in range(len(labels)):
    if labels[x] == 1:
        ax.scatter(sepallength[x],sepalwidth[x],petallength[x],marker='v',c='r')
    elif labels[x] == 2:
        ax.scatter(sepallength[x],sepalwidth[x],petallength[x],marker='o',c='b')
    elif labels[x] == 3:
        ax.scatter(sepallength[x],sepalwidth[x],petallength[x],marker='h',c='y')
ax.set_xlabel('Sepal length')
ax.set_ylabel('Sepal width')
ax.set_zlabel('Petal length')
plt.show()
f.close()

testlabels = []
f = open('irisData/testLabels.data')
word = f.readline()
while (word != ''):
    testlabels.append(int(word))
    word = f.readline()
f.close()
k=20
f = open('irisData/testData.data')
word = f.readline().strip().split(',')
outlabels = []
while (word[0] != ''):
    dist = []
    for x in range(len(sepallength)):
        dist.append(distance(word,sepallength[x],sepalwidth[x],petallength[x],petalwidth[x]))
    mini = dist[0]
    minpos = 0
    labels2 = []
    for x in range(k):
        mini = dist[0]
        minipos = 0
        for y in range(len(dist)):
            if (dist[y] < dist[minpos]):
                mini = dist[y]
                minipos = y
        dist[minipos] = float("inf")
        labels2.append(labels[minipos])
    one = 0
    two = 0
    three = 0
    for x in range(k):
        if(labels2[x] == 1):
            one = one+1
        if(labels2[x] == 2):
            two = two+1
        if(labels2[x] == 3):
            three = three+1
    print str(one),str(two),str(three)
    if(one == two):
        if(three > two):
            outlabels.append(3)
        else:
            outlabels.append(1)
    elif(two == three):
        if(one > two):
            outlabels.append(1)
        else:
            outlabels.append(2)
    elif(one == three):
        if(two > one):
            outlabels.append(2)
        else:
            outlabels.append(1)
    elif(one > two):
        if(one > three):
            outlabels.append(1)
        else:
            outlabels.append(3)
    elif(two > three):
        if(two > one):
            outlabels.append(2)
        else:
            outlabels.append(3)
    else:
        outlabels.append(3)
    print outlabels
    word = f.readline().strip().split(',')
print outlabels
print testlabels
errors = 0
for x in range(len(outlabels)):
    if (outlabels[x] != testlabels[x]):
        errors = errors +1
print errors
gc.collect()
           
                