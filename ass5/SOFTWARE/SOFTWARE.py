# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 19:39:35 2016

@author: kameelperd64
"""

import csv
import math

class Node:
    def __init__(self,value,leaf,name):
        self.name = name
        self.leaf = leaf
        self.value = value
        self.children = []

def entropy(data,y):
    global outcomes
    global ioutcomes
    global arroutcomes
    global categories
    global categoriescount

    entropy = 0
    
    
    split(data,y)  
    totalcount = 0
    for k in categoriescount:
        totalcount = totalcount + k      
    for x in range(len(outcomes)):
        for a in range(len(categories)): 
            count = 0
            for z in range(len(data)):
                if data[z][y] == categories[a] and data[z][len(data[0])-1] == outcomes[x]:
                    count = count +1
            prob = float(count)/float(categoriescount[a])
            
            
            tcount = float(count)/float(totalcount)
            if prob == 0:
                ent = 0
            else:
                ent = float(math.log(prob,2))
                
            entropy = entropy - tcount*prob*ent
    
    return entropy
        
        
def split(data,y):
    global categories
    global categoriescount
    categories = []
    categoriescount = [] 
    length = len(data)
    
    for x in range(length):
        for z in range(len(categories)):
            if data[x][y] == categories[z]:
                categoriescount[z] = categoriescount[z]+1
                break
        else:
            categories.append(data[x][y])
            categoriescount.append(1) 
     
        
def getOutcomes(data):
    global outcomes
    global ioutcomes
    global arroutcomes
    outcomes = []
    arroutcomes = []
    ioutcomes = 0
    for x in range(len(data)):
        for y in range(len(outcomes)):
            if data[x][len(data[0])-1] == outcomes[y]:
                arroutcomes[y] = arroutcomes[y]+1
                break
        else:
            outcomes.append(data[x][len(data[0])-1])
            arroutcomes.append(1)
            ioutcomes = ioutcomes+1


def ID3(data,category):
    global categories
    global categoriescount
    entropies = []
    
    for x in range(len(data[0])-1):
        entropies.append(entropy(data,x))
    
    lowest = 0
    for x in range(len(entropies)):
        if entropies[x] < entropies[lowest]:
            lowest = x
    
    
    
    totalentropy = 0.0
    for ent in entropies:
        totalentropy = totalentropy + float(ent)
    if totalentropy == 0:
        return Node(-1,data[0][len(data[0])-1],category)
        
    node = Node(lowest,None,category)
    split(data,lowest)
    length = len(categories)
    for x in range(length):
        split(data,lowest)
        newdata = [[' ' for c in range(len(data[0])-1)] for c in range(categoriescount[x])]
        a = 0
        b = 0
        for y in range(len(data)):
            for z in range(len(data[0])):
                if z == lowest:
                    continue
                if data[y][lowest] != categories[x]:
                    a = a -1
                    break                      
                newdata[a][b] = data[y][z]
                b = b +1
                    
            b = 0
            a = a+1
        node.children.append(ID3(newdata,categories[x]))
    return node
 
def Search(node,data):
    if node.value == -1:
        return node.leaf
    newdata = []
    for x in range(len(data)):
        if x == node.value:
            continue
        newdata.append(data[x])
    
    for x in range(len(node.children)):
        if data[node.value] == node.children[x].name:
            return Search(node.children[x],newdata)
    print "Input Error"
    return None
        
        
        


   
data = list(csv.reader(open('restaurant.csv')))
for x in range(len(data)):
    for y in range(len(data[0])):
        data[x][y] = data[x][y].strip()

getOutcomes(data)
head = ID3(data,None)
data = ['Yes','No','Yes','Yes','Full','$$','Yes','No','Thai','30-60']
data2 = ['No','No','Yes','Yes','Full','$$','Yes','No','Thai','30-60']
print Search(head,data)
print Search(head,data2)

