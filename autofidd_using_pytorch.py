# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 23:47:07 2021

@author: Mahfuz_Shazol
"""


#calculate dy/dx at x=5   here y=x^2

import torch as th

x=th.tensor(5.0)

print(x)

x.requires_grad_()

y=x**2

#use autodiff
y.backward()

result = x.grad

print(result)

