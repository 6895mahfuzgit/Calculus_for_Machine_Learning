# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 00:02:19 2021

@author: Mahfuz_Shazol
"""

import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(-10,10,1000)

#function y=x^2+2x+2
y=x**2+2*x+2

fig,ax=plt.subplots()
_ =ax.plot(x,y)



fig,ax=plt.subplots()
ax.set_xlim([-2,0])
ax.set_ylim([0,2])
_ =ax.plot(x,y)


fig,ax=plt.subplots()
ax.set_xlim([-1.5,-0.5])
ax.set_ylim([0.5,1.5])
_ =ax.plot(x,y)


fig,ax=plt.subplots()
ax.set_xlim([-1.1,-0.9])
ax.set_ylim([0.9,1.1])
_ =ax.plot(x,y)


fig,ax=plt.subplots()
ax.set_xlim([-1.01,-0.99])
ax.set_ylim([0.99,1.01])
_ =ax.plot(x,y)








