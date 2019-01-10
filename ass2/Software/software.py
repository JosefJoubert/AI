# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 14:02:21 2016

@author: kameelperd64
"""
import math
import matplotlib.pyplot as plt

class Node:
    def __init__(self):
        self.cost = 0.0
        self.heuristic = 0.0
        self.wall = 0
        self.visited = 0
        self.x = 0
        self.y = 0
        self.str = ""
        self.path = 0
        self.pathsx = []
        self.pathsy = []
        

def getNodes(num1,num2):
    global map
    nodes = [] 
    if (num1 != 0):#links op
        if (num2 != 11):
            if (map[num1-1][num2+1].wall == 0):
                if (map[num1-1][num2+1].visited == 0):
                    nodes.append(map[num1-1][num2+1])
                    nodes[len(nodes)-1].cost = math.sqrt(2)
    if (num2 != 11): #op
        if (map[num1][num2+1].wall == 0):
            if (map[num1][num2+1].visited == 0):
                nodes.append(map[num1][num2+1])
                nodes[len(nodes)-1].cost = 1
    if (num1 != 11): #regs op
        if (num2 != 11):
            if (map[num1+1][num2+1].wall == 0):
                if (map[num1+1][num2+1].visited == 0):
                    nodes.append(map[num1+1][num2+1])
                    nodes[len(nodes)-1].cost = math.sqrt(2)
    if (num1 != 11):#regs
        if (map[num1+1][num2].wall == 0):
            if (map[num1+1][num2].visited == 0):
                nodes.append(map[num1+1][num2])
                nodes[len(nodes)-1].cost = 1
    if (num1 != 11):#regs af
        if (num2 != 0):
            if (map[num1+1][num2-1].wall == 0):
                if (map[num1+1][num2-1].visited == 0):
                    nodes.append(map[num1+1][num2-1])
                    nodes[len(nodes)-1].cost = math.sqrt(2)
    if (num2 != 0):#af
        if (map[num1][num2-1].wall == 0):
            if (map[num1][num2-1].visited == 0):
                nodes.append(map[num1][num2-1])            
                nodes[len(nodes)-1].cost = 1     
    if (num1 != 0):#links af
        if (num2 != 0):
            if (map[num1-1][num2-1].wall == 0):
                if (map[num1-1][num2-1].visited == 0):
                    nodes.append(map[num1-1][num2-1])
                    nodes[len(nodes)-1].cost = math.sqrt(2)
    if (num1 != 0):#links
        if (map[num1-1][num2].wall == 0):
            if (map[num1-1][num2].visited == 0):
                nodes.append(map[num1-1][num2])
                nodes[len(nodes)-1].cost = 1     
    
    return nodes
    

    
def UCS(node):
    global visited
    global cost
    global time
    visited = visited + 1
    node.path = 1
    cost = cost + node.cost
    if (node.x == 9):
        if (node.y == 9):
            return
    
    #print cost
    node.visited = 1    
    nodes = getNodes(node.x,node.y)
    if (len(nodes) == 0):
        print "Error."
        return
    temp = nodes[0]
    for curr in nodes:
        curr.str = node.str + "[" + str(curr.x) + "," + str(curr.y) + "]"
        time = time+1
        if curr.cost < temp.cost:
            temp = curr
    #print str(node.x) + "," + str(node.y)
    print len(nodes)
    UCS(temp)
           
def getHeuristic(node):
    x = math.sqrt(pow(9-node.x,2)+pow(9-node.y,2))
    return x
    
def GS(node):
    global visited
    global cost
    global time
    cost = cost + node.cost
    visited = visited + 1
    node.path = 1
    global nodelist
    #print str(node.x) + "," + str(node.y)
    if (node.x == 9):
        if (node.y == 9):
            return
    node.visited = 1
    nodes = getNodes(node.x,node.y)
    temp = nodes[0]
    currHeuristic = getHeuristic(nodes[0])
    
    for curr in nodes:
        time = time+1
        curr.str = node.str + "[" + str(curr.x) + "," + str(curr.y) + "]"
        tempHeuristic = getHeuristic(curr)
        if (currHeuristic > tempHeuristic):
            temp = curr
            currHeuristic = tempHeuristic
    GS(temp)
            
def AStar(node):
    #print str(node.x) + "," + str(node.y)
    
    global visited
    visited = visited + 1
    global time
    #print str(node.x) + "," + str(node.y)
    if (node.x == 9):
        if (node.y == 9):
            return
    remove(node)
    global cost
    node.visited = 1
    nodes = getNodes(node.x,node.y)
    for curr in nodes:
        time = time+1
        curr.str = node.str + "[" + str(curr.x) + "," + str(curr.y) + "]"
        curr.cost = curr.cost + node.cost
        curr.pathsx.extend(node.pathsx)
        curr.pathsy.extend(node.pathsy)
        curr.pathsx.append(node.x)
        curr.pathsy.append(node.y)
        nodelist.append(curr)
    temp = nodelist[0]
    for curr in nodelist:
        if (temp.cost+temp.heuristic) > (curr.cost + curr.heuristic):
            temp = curr
    
    AStar(temp)
    
def remove(node):
    global nodelist
    templist = []
    for curr in nodelist:
        if curr != node:
            templist.append(curr)
    nodelist = templist

def reset():
    global map
    global visited
    global cost
    global time
    for x in range(0,12):
        for y in range(0,12):
            map[x][y].visited = 0
            map[x][y].str = ""
            map[x][y].cost = 0
            map[x][y].path = 0
    map[0][0].str = "[0,0]"
    visited = 0
    cost = 0
    time = 0
 
def plot():
    global map
    fig = plt.figure()
    for x in range(0,12):
        for y in range(0,12):
            if (map[x][y].path == 1):
                plt.plot(x,y,'rs')
            elif (map[x][y].visited == 1):
                plt.plot(x,y,'gs')
            elif (map[x][y].wall == 1):
                plt.plot(x,y,'ks')
            else:
                plt.plot(x,y,'ws')
            
            
    plt.axis([-1,12,-1,12])
    plt.show
      
global map
map = [[Node() for x in range(12)] for x in range(12)]
global walls
walls = [[0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,1,1,1,0,1,1,0],
         [0,1,0,0,0,0,1,1,0,1,1,0],
         [0,1,1,0,0,0,0,0,0,1,1,0],
         [0,1,1,1,0,0,0,0,0,1,1,0],
         [0,1,1,1,1,0,0,0,0,1,1,0],
         [0,1,1,1,1,1,1,1,1,1,1,0],
         [0,1,1,1,1,1,1,1,1,1,1,0],
         [0,0,0,0,0,0,0,0,0,0,1,0],
         [0,0,0,0,0,0,0,0,0,0,1,0],
         [0,0,1,1,1,1,1,1,1,1,1,0],
         [0,0,0,0,0,0,0,0,0,0,0,0]]
for x in range(0,12):
    for y in range(0,12):
        map[x][y].x = x
        map[x][y].y = y
        if walls[x][y] == 1:
            map[x][y].wall = 1
global cost
global visited
global time
time = 0
visited = 0
cost = 0
map[0][0].str = "[0,0]"
print "Starting Uniform Cost Search:"
UCS(map[0][0])
print "Complete. Cost: " + str(cost)
print "Path:"
print map[9][9].str
print "Nodes visited: " + str(visited)
print "Time: " + str(time)
plot()
reset()
print "Starting Greedy Search:"
GS(map[0][0])
print "Complete. Path:"
print map[9][9].str
print "Nodes visited: " + str(visited)
print "Total cost: " + str(cost)
print "Time: " + str(time)
global nodelist
nodelist = []
nodelist.append(map[0][0])
cost = 0
plot()
reset()
print "Starting A* search:"
AStar(map[0][0])
print "Search complete. Path:"
print map[9][9].str
print "Nodes visited: " + str(visited)
for x in range(0,len(map[9][9].pathsx)):
    map[map[9][9].pathsx[x]][map[9][9].pathsy[x]].path = 1
map[0][0].path = 1
print "Total cost: " + str(map[9][9].cost)
print "Time: " + str(time)
plot()
