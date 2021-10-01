# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 22:59:11 2021

@author: Mahfuz_Shazol
"""

import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(-10,10,1000)


#function y=x^2+2x+2
def f(x):
    x=x**2+2*x+2
    return x

x_delta=0.000001
x=-1

#find the slop  of x=-1
y=f(x)
print('y:',y)

#the point P is (-1,1)
x2=x+x_delta
print('x2 :',x2)
y2=f(x2)
print('y2 :',y2)

m=(y2-y)/(x2-x)
print('m :',m)










