# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import googlemaps
gmaps = googlemaps.Client(key='AIzaSyAVz0wSdqPU3bV3y_tJCmV_uLmeZeHy_AQ')

class Node:
    def __init__(self,value,loc,children=[]):
        self.value = value
        self.children = children
        self.loc = loc


def build(node,loc = []):
    print "build has been called with:"
    print loc
    node.children = []
    for child in node.children:
        print child.loc
    if len(loc) == 0:
        node1 = Node(5,"University of Pretoria, Pretoria",[])
        node.children.append(node1)
        return 0        
    for location in loc:
        #print location
        node1 = Node(5,location)
        node.children.append(node1)
        loc2 = loc
        loc2.remove(location)
        build(node1,loc2)
        
                          

locations = ["University of Pretoria, Pretoria","CSIR, Meiring Naude Road, Pretoria","Armscor, Delmas Road, Pretoria","Denel Dynamics, Nellmapius Drive, Centurion","Air Force Base Waterkloof, Centurion"]
locations2 = ["CSIR, Meiring Naude Road, Pretoria","Armscor, Delmas Road, Pretoria","Denel Dynamics, Nellmapius Drive, Centurion","Air Force Base Waterkloof, Centurion"]
tree = Node(0,locations[0],[])
build (tree,locations2)

for child in tree.children:
    print child.loc
print ","
for child in tree.children[0].children:
    print child.loc
print ","
for child in tree.children[0].children[0].children:
    print child.loc
for child in tree.children[0].children[0].children[0].children:
    print child.loc
