# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 23:04:34 2021

@author: ASUS
"""

import numpy as np
import matplotlib.pyplot as plt
import time
start_time = time.time()

def func(x, y): # defining the main function
    u, v = y+y**2, -x/2+y/5-x*y+(y**2)*6/5
    return u, v


# half length of dimension in x and y axis
l = 10


n =2*l*40 # number of points along x/y axis


# X and Y dimensions
x = np.linspace(-l, l, n)
y = np.linspace(-l, l, n)

# Creating a mesh field
X, Y = np.meshgrid(x, y)

# Calculating velocities
U, V = func(X, Y)

vel = (U**2 + V**2)**0.5
plt.figure()

#to show the phase portrait
stream = plt.streamplot(X, Y,                  # x and y coordinate positions
               U, V,                    # u and v velocities
               arrowsize=2,
               arrowstyle='->',
               color=vel,
               density=5,
               linewidth=1,
               cmap=plt.cm.jet
               )


plt.title("two eyed monster ")
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(stream.lines)
plt.xticks()
plt.yticks()
plt.grid()


for i in range (1,len(X)): #to show the nullclines
    for j in range (1,len(X[1])):
        
        if (U[i][j]*U[i-1][j])<=0 or (U[i][j]*U[i][j-1])<=0 : #when the sign is changing btween two neighbors
            plt.scatter(X[i][j], Y[i][j], s=3,color=(0,1,0))
        
        if (V[i][j]*V[i-1][j])<=0 or (V[i][j]*V[i][j-1])<=0:
            plt.scatter(X[i][j], Y[i][j], s=3,color=(1,0,0))
            

for i in range (1,len(X)): # to show the fixed point
    for j in range (1,len(X[1])):
        if (U[i][j]*U[i-1][j])<=0 or (U[i][j]*U[i][j-1])<=0 :
            if (V[i][j]*V[i-1][j])<=0 or (V[i][j]*V[i][j-1])<=0:
                print ('boom')
                plt.scatter(X[i][j], Y[i][j], s=200,color=(.5,0,.5))
plt.show()
print("--- %s seconds ---" % (time.time() - start_time)) #runtime