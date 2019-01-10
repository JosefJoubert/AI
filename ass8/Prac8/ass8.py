from math import *
import csv
import random

#Define the sigmoid functions
#f= lambda x:    1/(1+exp(-float(x)))
def f(x):
    try:
        return 2/(1+exp(-x)) - 1
    except OverflowError:
        if (x<0):
            return 0
        else:
            return 1
            
def f(x):
    try:
        return 1/(1+exp(-x)) * (1-1./(1+exp(-x)))
    except OverflowError:
        return 0

def BackProp(inputdata,targets,learning,terminate):
    global weights1
    global weights2
    global biasweight1
    global biasweight2
    features = len(inputdata)
    Errors = []
    epoch2 = 0
    hidden = [float(0) for i in range(len(weights1))]
    outputneurons = [float(0) for i in range(len(targets))]
    epoch = 0
    while(1==1):
        hidden = [float(0) for i in range(len(weights1))]
        outputneurons = [float(0) for i in range(len(targets))]
        for hid in range(len(hidden)):
            for x in range(features):
                hidden[hid] = hidden[hid] + inputdata[x][epoch]*weights1[x][hid]
            hidden[hid] = hidden[hid] + 1*biasweight1[hid]
            #hidden[hid] = f(hidden[hid])
        for out in range(len(outputneurons)):
            for x in range(len(hidden)):
                outputneurons[out] = outputneurons[out] + f(hidden[x])*weights2[x][out]
            outputneurons[out] = outputneurons[out] + 1*biasweight2[out]
            #outputneurons[out] = f(outputneurons[out])
        sumerror = []
        error = 0
        for tar in range(len(targets)):
            func = f(outputneurons[tar])
            temp = float(targets[tar][epoch])-func
            sumerror.append(temp) 
            error = error + temp
        Errors.append(error**2/2)
        dz = []
        for x in range(len(outputneurons)):
            
            dz.append(sumerror[x]*df(outputneurons[x]))
        dh = []
        for x in range(len(hidden)):
            error = 0
            for y in range(len(outputneurons)):
                error = error + weights2[x][y]*dz[y]
            dh.append(error*df(hidden[x]))
            #print error*df(hidden[x])
        for x in range(len(hidden)):
            for y in range(len(outputneurons)):
                weights2[x][y] = weights2[x][y] + learning*f(hidden[x])*dz[y]
        for x in range(len(inputdata)):
            for y in range(len(hidden)):
                weights1[x][y] = weights1[x][y] + learning*inputdata[x][epoch]*dh[y]
        for x in range(len(biasweight1)):
            biasweight1[x] = biasweight1[x] + learning*1*dh[x]
        for x in range(len(biasweight2)):
            biasweight2[x] = biasweight2[x] + learning*dz[x]
        if (len(Errors) > 1):
            if(abs(Errors[len(Errors)-1] - Errors[len(Errors) - 2]) < terminate):
                print "Break because of error"
                break   
        epoch = epoch + 1
       
        if (epoch == 720):
            #print "Break because of epoch"
            break
            print epoch2
            epoch = 0
            epoch2 = epoch2 +1
            if (epoch2 == 1000):
                break
        #print Errors
    return Errors

def ffNeuralNet(inputs):
    global weights1
    global weights2
    global biasweight1
    global biasweight2
    hidden = [float(0) for i in range(len(inputs))]
    for x in range(len(hidden)):
        for y in range(len(hidden)):
            hidden[x] = hidden[x] + inputs[y]*weights1[y][x]
        hidden[x] = hidden[x] + biasweight1[x]
        hidden[x] = f(hidden[x])
    output = 0
    for y in range(len(hidden)):
        output = output + hidden[y]*weights2[y][0]
    output = output + biasweight2[0]
    output = f(output)
    return output
    
    
    

global weights1
global weights2
global biasweight1
global biasweight2
inputdata = list(csv.reader(open('q2inputs.csv')))  
targets = list(csv.reader(open('q2targets.csv')))
for x in range(len(inputdata)):
    for y in range(len(inputdata[0])):
        inputdata[x][y] = f(float(inputdata[x][y]))
weights1 = [[2*random.random()-1 for i in range(len(inputdata))] for j in range(len(inputdata))]
weights2 = [[2*random.random()-1 for i in range(len(targets))] for j in range(len(inputdata))]
biasweight1 = [2*random.random()-1 for i in range(len(weights1))]
biasweight2 = [2*random.random()-1 for i in range(len(targets))]
print weights1
print weights2
learningrate = 0.1
terminate = 0.0000000000000001
BackProp(inputdata,targets,learningrate,terminate)
print weights1
print weights2
data = [[float(0) for i in range(16)] for j in range(16)]
for x in range(16):
    for y in range(16):
        data[x][y] = ffNeuralNet([x,y])
print data
