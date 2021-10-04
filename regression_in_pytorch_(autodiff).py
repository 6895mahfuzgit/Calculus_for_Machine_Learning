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

m=th.tensor([0.9]).requires_grad_()
print(m)

b=th.tensor([0.1]).requires_grad_()
print(b)


def regression_plot(my_x,my_y,my_m,my_b):
    
    fig,ax=plt.subplots()
    ax.scatter(my_x,my_y)
    x_min,x_max=ax.get_xlim()
    y_min,y_max=my_m*x_min+my_b,my_m*x_max+my_b
    ax.set_xlim([x_min,x_max])
    _=ax.plot([x_min,x_max],[y_min,y_max])


regression_plot(x, y, m, b)    