import math
from operator import attrgetter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
from random import randint

def read_file (file):

    d = []

    ifile  = open(file + ".data", 'r')
    
    for raw_row in ifile.read().splitlines():
            
        row = raw_row.split(',')
        temp_row = []

        for item in row:
            temp_row.append(float(item))

        d.append(temp_row)

    return d


testData = read_file('testData')
testLabels = read_file('testLabels')

trainData = read_file('trainData')
trainLabels = read_file('trainLabels')


def define_flower(n):

    if n==1:
        return "Iris Setosa"

    if n==2:
        return "Iris Versicolour"

    if n==3:
        return "Iris Virginica"


def distance(p1,p2):

    dimensions = len(p1)

    summation = 0

    for dimension in range(dimensions):

        temp = math.pow(p1[dimension] - p2[dimension],2) 
        summation = summation + temp

    return math.sqrt(summation)


def nearest_neighbours(k,master,data,label):

    temp = []

    for item in range(len(data)):

        dis = distance(master,data[item])

        lab = define_flower(label[item][0])

        temp.append([data[item],lab,dis])

    temp2 = sorted(temp, key=lambda l:l[2], reverse=False)
    temp2.pop(0)

    neighbours = []

    for i in range(k):

        neighbours.append(temp2[i])

    return neighbours


def most_type (neighbours):

    count1 = 0
    count2 = 0
    count3 = 0


    for i in neighbours:

        if i[1] ==  "Iris Setosa":

            count1 += 1

        if i[1] == "Iris Versicolour" :

            count2 += 1

        if i[1] == "Iris Virginica" :

             count3 += 1

    if count1 > count2 and count1 > count3 :

        return "Iris Setosa"

    if count2 > count1 and count2 > count3 :

        return "Iris Versicolour" 
    
    if count3 > count2 and count3 > count1 :

        return "Iris Virginica" 

    else : 

        "ERROR ?!"
