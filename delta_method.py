# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 21:15:00 2021

@author: Mahfuz_Shazol
"""


import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(-10,10,1000)


#function y=x^2+2x+2
def f(x):
    x=x**2+2*x+2
    return x

y=f(x)
fig,ax=plt.subplots()

plt.axvline(x=0,color='lightgray')
plt.axhline(y=0,color='lightgray')

print(f(2))
plt.scatter(2, 10)

print(f(7))
plt.scatter(7, 65)

#slop m
#m=(y2-y1)/(x2-x1)
m=(65-10)/(7-2)
print(m)

#y=mx+c
#c=y-mx
c=65-(11*7)

#Y lines
line_y=(11*x)-12
print(line_y)

plt.plot(x,line_y,c='orange')

print(c)



_ =ax.plot(x,y)






