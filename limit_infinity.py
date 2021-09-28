# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 16:11:38 2021

@author: Mahfuz_Shazol
"""

import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(-10,10,1000)

#lim x->infinity =25/x 
def calculate(x):
    x=25/x
    return x


y=calculate(x)
fig,ax=plt.subplots()

plt.axvline(x=0,color='lightgray')
plt.axhline(y=0,color='lightgray')

plt.xlim(-10,10)
plt.ylim(-300,300)

plt.axvline(x=0,color='purple',linestyle='--')
plt.axhline(y=1,color='purple',linestyle='--')

_ =ax.plot(x,y)
