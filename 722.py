# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 22:59:01 2021

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import time
start_time = time.time()

def vol(x, y): # defining the main function
    vol= x**2 - y**2
    return vol

def gradvol (x,y):
    d=2*l/n
    u= vol (x+d,y)-vol(x, y)
    v= vol(x, y+d)- vol(x, y)
    return (u,v)

def sin_arr(arr): 
    l1,l2=len(arr),len(arr[1])
    sin=np.zeros((l1,l2))
    for i in range (0,l1):
        for j in range (0,l2):
            sin[i][j]=math.sin(arr[i][j])
    return (sin)

def cos_arr(arr):
    l1,l2=len(arr),len(arr[1])
    cos=np.zeros((l1,l2))
    for i in range (0,l1):
        for j in range (0,l2):
            cos[i][j]=math.cos(arr[i][j])
    return (cos)

# half length of dimension in x and y axis
l = 10


n =2*l*10 # number of points along x/y axis


# X and Y dimensions
x = np.linspace(-l, l, n)
y = np.linspace(-l, l, n)

# Creating a mesh field
X, Y = np.meshgrid(x, y)

# Calculating velocities
U, V = gradvol(X, Y)

vel = (U**2 + V**2)**0.5
plt.figure(dpi=100)


stream = plt.streamplot(X, Y,                  # x and y coordinate positions
               U, V,                    # u and v velocities
               arrowsize=2,
               arrowstyle='->',
               color=vel,
               density=3,
               linewidth=1,
               cmap=plt.cm.jet
               )


plt.title("7.2.2 ")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(stream.lines)
plt.xticks()
plt.yticks()
plt.grid()


for i in range (1,len(X)):
    for j in range (1,len(X[1])):
        
        if (U[i][j]*U[i-1][j])<=0 or (U[i][j]*U[i][j-1])<=0 :
            plt.scatter(X[i][j], Y[i][j], s=3,color=(0,1,0))
        
        if (V[i][j]*V[i-1][j])<=0 or (V[i][j]*V[i][j-1])<=0:
            plt.scatter(X[i][j], Y[i][j], s=3,color=(1,0,0))
            

for i in range (1,len(X)): # comes in front of other dots
    for j in range (1,len(X[1])):
        if (U[i][j]*U[i-1][j])<=0 or (U[i][j]*U[i][j-1])<=0 :
            if (V[i][j]*V[i-1][j])<=0 or (V[i][j]*V[i][j-1])<=0:
                print ('boom')
                plt.scatter(X[i][j], Y[i][j], s=200,color=(.5,0,.5))
plt.show()
print("--- %s seconds ---" % (time.time() - start_time)) #runtime
#plt.savefig("722")