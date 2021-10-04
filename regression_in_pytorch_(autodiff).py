# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 00:11:25 2021

@author: Mahfuz_Shazol
"""

import torch as th
import matplotlib.pyplot  as plt

x=th.tensor([0,1.,2.,3.,4.,5.,6.,7.])
print(x)

y=-0.5*x+2+th.normal(mean=th.zeros(8), std=0.2)
print(y)


fix,ax=plt.subplots()
plt.title('Clinical Trial')
plt.xlabel('Drug dose (mL)')
plt.ylabel('Forgetfullness')
_=ax.scatter(x,y)