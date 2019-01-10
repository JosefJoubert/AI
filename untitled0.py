# -*- coding: utf-8 -*-
"""
Created on Tue May 31 18:31:29 2016

@author: kameelperd64
"""

from numpy import *
import matplotlib.pyplot as plt
#Sigmoid f u n c ti o n
d e f si gm oid ( x ) :
y = 1/(1+ exp(−x ) )
r e t u r n y
#Dimensions
D = 2
N = 10
#C re a te random sample s .
#Cl a s s 0 c o n t i a i n s 5 s ample s randomly d i s t r i b u t e d o ve r the l o c a t i o n ( 0 . 5 , 0 . 5 )
#Cl a s s 1 c o n t i a i n s 5 s ample s randomly d i s t r i b u t e d o ve r the l o c a t i o n ( 2 . 5 , 2 . 5 )
X =random . rand (D,N)
X[ : , 5 : 1 0 ] = X[ : , 5 : 1 0 ] + 2∗ one s ( (D, 5 ) )
#Add the row o f bi a s v al u e s
X = c o n c a t e n a t e ( (X, one s ( ( 1 ,N) ) ) , a x i s =0)
D = 3
#C re a te the v e c t o r o f output l a b e l s
c = a r r a y ( [ [ 0 . 0 ] , [ 0 . 0 ] , [ 0 . 0 ] , [ 0 . 0 ] , [ 0 . 0 ] , [ 1 . 0 ] , [ 1 . 0 ] , [ 1 . 0 ] , [ 1 . 0 ] , [ 1 . 0 ] ] )
#I n i t i a l i s e w ei g h t s t o random v al u e s
w = random . rand (D, 1 )
w = z e r o s ( (D, 1 ) )
#Se t the l e a r n i n g r a t e
e t a = 0. 2
p r i n t ( ’ \nX=’ )
p r i n t (X)
7
p r i n t ( ’ \nc=’ )
p r i n t ( c )
p r i n t ( ’ \nw=’ )
p r i n t (w)
p r i n t ( ’ \ ne t a=’ )
p r i n t ( e t a )
#I n i t i a l i s e the pl o t
p l t . c l o s e ( ’ a l l ’ )
p l t . f i g u r e ( )
#Number o f al g o ri t hm i t e r a t i o n s
num I ters = 100
#I n i t i a l i s e the memory f o r the e r r o r .
e n d I t e r = i t e r a t i o n s
J = z e r o s ( ( numIters , 1 ) )
#G r adien t d e s c e n t l o o p
f o r i t e r a t i o n i n r an ge ( 0 , num I ters ) :
#Compute the output o f the l o g i s t i c r e g r e s s i o n f u n c ti o n
o = si gm oid ( dot (X. T,w) )
#Compute the e r r o r
J [ i t e r a t i o n ] = 0. 5 ∗ dot ( t r a n s p o s e ( c−o ) , ( c−o ) )
#Compute the wei gh t upd a te s
dw = dot (X, ( c − si gm oid ( dot (X. T,w ) ) ) )
#Update the w ei g h t s
w = w + e t a ∗dw
#P ri n t out the r e s u l t s
p r i n t ( ’ \n\nITERATION %i \n ’ % i t e r a t i o n )
p r i n t ( ’ \noutput=’ )
p r i n t ( o )
p r i n t ( ’ \nJ=’ )
p r i n t ( J [ i t e r a t i o n ] )
p r i n t ( ’ \ndw=’ )
p r i n t (dw)
p r i n t ( ’ \nw=’ )
p r i n t (w)
#Pl o t the r e s u l t s
p l t . c l a ( )
p l t . pl o t (X[ 0 , 0 : 5 ] , X[ 1 , 0 : 5 ] , ’b∗ ’ )
p l t . pl o t (X[ 0 , 5 : 1 0 ] , X[ 1 , 5 : 1 0 ] , ’ r o ’ )
x0 = [ 0 , 3 ]
x1 = (−w[ 0 ] ∗ x0 − w[ 2 ] ) / (w[ 1 ] )
p l t . pl o t ( x0 , x1 )
p l t . pause ( 0 . 1 )
p l t . draw ( )
#Terminating c o n di ti o n
i f ( i t e r a t i o n > 0 ) :
i f ( abs ( J [ i t e r a t i o n ] − J [ i t e r a t i o n −1]) < 0 . 0 0 1 ) :
e n d I t e r = i t e r a t i o n
p r i n t ( ’ \ nTerminating \n ’ )
break ;
#Pl o t the e r r o r
p l t . f i g u r e ( )
p l t . pl o t ( J [ 0 : e n d I t e r ] )