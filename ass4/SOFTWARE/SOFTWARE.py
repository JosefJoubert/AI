# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:17:15 2016

@author: kameelperd64
"""
import sys
import copy

class Node:
    def __init__(self,minmax,state):
        self.minmax = minmax
        self.value = 0
        self.children = []
        self.state = state
        self.terminal = 0

class AlphaBeta:
    def __init__(self,head):
        self.head = head
        #print head.state
    
    def AlphaBetaSearch(self):
        x = self.MaxValue(self.head,-sys.maxint,sys.maxint)
        #print x
        for child in self.head.children:
            #print child.value
            if child.value == x:
                self.head = child
                return child
                
    def AlphaBetaSearch2(self):
        x = self.MinValue(self.head,-sys.maxint,sys.maxint)
        #print x
        for child in self.head.children:
            #print child.value
            if child.value == x:
                self.head = child
                return child
            
        
    def MaxValue(self,node,alpha,beta):
        #print node.state
        if node.terminal != 0:
            node.value = node.terminal
            return node.terminal
        if len(node.children) == 0:
            return 0
        v = -sys.maxint
        #print node.children
        for child in node.children:
            v = max(v,self.MinValue(child,alpha,beta))
            if v >= beta:
                #print "MaxValue Prune Return: " + str(v)
                node.value = v
                return v
            alpha = max(alpha,v)
        #print "MaxValue Normal Return: " + str(v)
        node.value = v
        #print self.head.children[2].state
        #print node.state
        return v
                
            
    
    def MinValue(self,node,alpha,beta):
        #print node.state
        if node.terminal != 0:
            node.value = node.terminal
            return node.terminal
        if len(node.children) == 0:
            return 0
        v = sys.maxint
        #print node.children
        for child in node.children:
            v = min(v,self.MaxValue(child,alpha,beta))
            if v <= alpha:
                #print "MinValue Prune Return: " + str(v)
                node.value = v
                return v
            beta = min(beta,v)
        #print "MinValue Normal Return: " + str(v)
        node.value = v
        return v
        

                    
        
    
def printstate(node):
    print  node.state[0][0] + " " + "|" + " " + node.state[0][1]   + " " + "|" + " "  +node.state[0][2] 
    print "---------"
    print node.state[1][0]   + " " + "|" + " "  + node.state[1][1]  + " " + "|" + " "  +node.state[1][2] 
    print "---------"
    print  node.state[2][0]   + " " + "|" + " "  + node.state[2][1]   + " " + "|" + " "  + node.state[2][2] 
    
def printboard(node):
    tempnode = Node(0,copy.deepcopy(node.state))
    arr = ["a","b","c","d","e","f","g","h","i"]
    z = 0
    for x in range(3):
        for y in range(3):
            if tempnode.state[x][y] == " ":
                tempnode.state[x][y] = arr[z]
                z = z+1
    printstate(tempnode)
    if z == 0:
        return 1
            
            
            

def TerminalTest(node):
   string = "X"
   for z in range(2):
       for x in range(3):
           for y in range(3):
               if (node.state[x][y] != string):
                   break
           else:
               if string == "X":
                   return 1
               else:
                   return -1
           for y in range(3):
               if (node.state[y][x] != string):
                   break    
           else:
               if string == "X":
                   return 1
               else:
                   return -1   
       string = "O"
   if node.state[0][0] == "X" and node.state[1][1] == "X" and node.state[2][2] == "X":
      return 1
   if node.state[0][2] == "X" and node.state[1][1] == "X" and node.state[2][0] == "X":
      return 1
   if node.state[0][0] == "O" and node.state[1][1] == "O" and node.state[2][2] == "O":
      return -1
   if node.state[0][2] == "O" and node.state[1][1] == "O" and node.state[2][0] == "O":
      return -1
      
   return 0
        
def build(node):
    node.terminal = TerminalTest(node)
    if (node.terminal != 0):
        return
    xarr = []
    yarr = []
    for x in range(3):
        for y in range(3):
          if node.state[x][y] == " ":
              xarr.append(x)
              yarr.append(y)

    for x in range(len(xarr)):
        tempstate = copy.deepcopy(node.state)
        
        if node.minmax == 1:
            tempnode = Node(0,tempstate)
            tempnode.state[xarr[x]][yarr[x]] = "X"
            node.children.append(tempnode)
        else:
            tempnode = Node(1,tempstate)            
            tempnode.state[xarr[x]][yarr[x]] = "O"
            node.children.append(tempnode)
    for x in range(len(xarr)):
        build(node.children[x])

        
state = [[" "," "," "],[" "," "," "],[" "," "," "]]
alphabet = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8}
head = Node(1,state)
print "Building game, this may take a minute."
build(head)
game = AlphaBeta(head)
printboard(head)
print "Please enter a,b,c,d,e,f,g,h or i to make a move, or type 'go' to let the AI go first:"
inputstr = raw_input()
if inputstr == "quit":
    sys.exit()

if inputstr == "go":
    while 1 ==1:
        game.head = game.AlphaBetaSearch()
        if TerminalTest(game.head) == 1:
            printboard(game.head)
            print "AI win. Play again?[y,n]"
            inputstr = raw_input()
            if inputstr == "y":
                game.head = head
                continue
            else:
                sys.exit()
        if printboard(game.head) == 1:
            print "Tie. Play again? [y,n]"
            inputstr = raw_input()
            if inputstr == "y":
                game.head = head
                continue
            else:
                sys.exit()
        while 1==1:
            print "Please enter a,b,c,d,e,f,g,h or i to make a move:"    
            inputstr = raw_input()
            if inputstr == "quit":
                sys.exit()
            inp = alphabet.get(inputstr)
            if inp == None:
                print "Invalid Input"
            else:
                game.head = game.head.children[inp]
                if TerminalTest(game.head) == 1:
                    print "You win. This is actually not possible. If you're reading this message you are a wizard. Please call me and tell me how you did this."
                    sys.exit()                    
                break
else:
    while 1==1:  
        if inputstr == "quit":
            sys.exit()
        inp = alphabet.get(inputstr)
        if inp == None:
            print "Invalid Input"
        else:
            game.head = game.head.children[inp]
            break
    game.head = game.AlphaBetaSearch2()
    printboard(game.head)
    while 1==1:
        while 1 == 1:            
            print "Please enter a,b,c,d,e,f,g,h or i to make a move:"    
            inputstr = raw_input()
            if inputstr == "quit":
                sys.exit()
            inp = alphabet.get(inputstr)
            if inp == None:
                print "Invalid Input"
            else:
                game.head = game.head.children[inp]
                if TerminalTest(game.head) == 1:
                    print "You win. This is actually not possible. If you're reading this message you are a wizard. Please call me and tell me how you did this."
                    sys.exit()                    
                break
        if len(game.head.children) == 0:
            print "Tie. Play again? [y,n]"
            inputstr = raw_input()
            if inputstr == "y":
                game.head = head
                continue
            else:
                sys.exit()
        game.head = game.AlphaBetaSearch2()
        printboard(game.head)
        if TerminalTest(game.head) == -1:
            print "AI win. Play again?[y,n]"
            inputstr = raw_input()
            if inputstr == "y":
                game.head = head
                printboard(game.head)
                continue
            else:
                sys.exit()
        
        
                        
del head

