# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:25:48 2016

@author: kameelperd64
"""
import googlemaps
gmaps = googlemaps.Client('AIzaSyATRIUPX1HUczj6VZwrEdPmG62ufZG1cpI')

class Node:
    def __init__(self,value,parent,loc,children=[]):
        self.value = value
        self.children = children
        self.parent = parent
        self.loc = loc
        self.shortest = 0
        

def Build(node,loc=[]):
    node.children = []
    for location in loc:
        node2 = node
        while 1 == 1:
            if node2 == None:
                dist = node.value + getDist(node.loc,location)
                node.children.append(Node(dist,node,location))
                break
            if (node2.loc == location):
                break
            node2 = node2.parent
    
    if len(node.children) == 0:
        dist = node.value + getDist(node.loc,"University of Pretoria, Pretoria")
        Distances.append(dist)
        node2 = Node(dist,node,"University of Pretoria, Pretoria")
        node2.shortest = 1
        for x in Distances:
            if x < node2.value:
                node2.shortest = 0
        
        if node2.shortest ==1 :
            global short            
            if short != None:
                short.shortest = 0
            short = node2
            #printroute(node2)
        node.children.append(node2)
        return
    
    x=0
    for child in node.children:
        node2 = node.children[x]
        Build(node2,loc)
        x = x+1
    
def Printtree(node):
     if node == None:
         return
    
     print node.loc + ":"
     string = "["
     for child in node.children:
         string = string + "," + child.loc + ","
     string = string + "]"
     print string
     for child in node.children:
         Printtree(child)

def getDist(loc1,loc2):    
    y = (gmaps.distance_matrix(loc1,loc2))['rows'][0]['elements'][0]['distance']['value']
    x = int(y)
    return x
    
def printroute(node):
    listloc = []
    node2 = node
    while node2 != None:
        listloc.append(node2.loc)
        node2 = node2.parent
    print "["
    for loc in reversed(listloc):
        print loc
    print "]"
    
def DFS(node):
    global visited
    visited = visited + 1
    global nodelist
    nodelist.pop(0)
    if node.shortest == 1:
        return node
    templist = reversed(node.children)
    for child in templist:
        nodelist.insert(0,child)
    return DFS(nodelist[0])

def BFS(node):
    global visited
    visited = visited +1
    if node.shortest == 1:
        return node
    global nodelist
    nodelist.pop(0)
    for child in node.children:
        nodelist.append(child)
    return BFS(nodelist[0])

def UCS(node):
    global visited
    visited = visited +1
    if node.shortest == 1:
        return node
    global nodelist
    for child in node.children:
        nodelist.append(child)
    node1 = nodelist[0]
    for node2 in nodelist:
        if node2.value < node1.value:
            node1 = node2
    nodelist.remove(node1)
    
    return UCS(node1)

loc2 = ["CSIR, Meiring Naude Road, Pretoria","Armscor, Delmas Road, Pretoria","Nellmapius Dr, Centurion, 0157","West Gate, Hans Strydom Drive, Lyttelton, Centurion, 0157"]
tree = Node(0,None,"University of Pretoria, Pretoria")
global Distances
global short
global nodelist
global visited
visited = 0
short = tree
nodelist = []
Distances = []
Build(tree,loc2)
nodelist.append(tree)
print "Starting DFS:"
shortnode = DFS(tree)
print "Shortest path found. Path:"
printroute(shortnode)
print "Distance:" + str(shortnode.value) + "m"
print "Nodes visited: " + str(visited)
visited = 0
nodelist = []
nodelist.append(tree)
print " "
print "Starting BFS:"
shortnode = BFS(tree)
print "Shortest path found. Path:"
printroute(shortnode)
print "Distance:" + str(shortnode.value) + "m"
print "Nodes visited: " + str(visited)
visited = 0 
print " "
print "Starting UCS:"
shortnode = UCS(tree)
print "Shortest path found. Path:"
printroute(shortnode)
print "Distance: " + str(shortnode.value) + "m"
print "Nodes visited: " + str(visited)

