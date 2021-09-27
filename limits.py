# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 02:08:23 2021

@author: Mahfuz_Shazol
"""

import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(-10,10,1000)

#function y=x^2+2x+2
y=x**2+2*x+2

fig,ax=plt.subplots()

plt.axvline(x=0,color='lightgray')
plt.axhline(y=0,color='lightgray')

plt.xlim(-5,10)
plt.ylim(-10,80)

plt.axvline(x=5,color='purple',linestyle='--')
plt.axhline(y=37,color='purple',linestyle='--')

_ =ax.plot(x,y)


