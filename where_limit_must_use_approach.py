# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 15:49:52 2021

@author: Mahfuz_Shazol
"""

import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(-10,10,1000)

#function y=sin(x)/x
def calculate(x):
    x=np.sin(x)/x
    return x


y=calculate(x)
fig,ax=plt.subplots()

plt.axvline(x=0,color='lightgray')
plt.axhline(y=0,color='lightgray')

plt.xlim(-10,10)
plt.ylim(-1,2)

plt.axvline(x=0,color='purple',linestyle='--')
plt.axhline(y=1,color='purple',linestyle='--')

_ =ax.plot(x,y)
