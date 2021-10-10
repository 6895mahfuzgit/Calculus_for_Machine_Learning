# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 00:25:24 2021

@author: Mahfuz_Shazol
"""
import torch as th
import matplotlib.pyplot  as plt


def refression(my_x, my_m, my_b):
    return my_m*my_x+my_b

def regression_plot(my_x,my_y,my_m,my_b):    
        fig,ax=plt.subplots()
        ax.scatter(my_x,my_y)
        x_min,x_max=ax.get_xlim()
        y_min,y_max=my_m*x_min+my_b,my_m*x_max+my_b
        ax.set_xlim([x_min,x_max])
        _=ax.plot([x_min,x_max],[y_min,y_max])


x = th.tensor([0, 1., 2., 3., 4., 5., 6., 7.])
print(x)

y = -0.5*x+2+th.normal(mean=th.zeros(8), std=0.2)
print(y)


m = th.tensor([0.9]).requires_grad_()
print(m)

b = th.tensor([0.1]).requires_grad_()
print(b)

# Forward pass(1)
yhat = refression(x, m, b)
print(yhat)


# Compare yhat with y actual value

def mse(my_yhat, my_y):
    sigma = th.sum((my_yhat-my_y)**2)
    return sigma/len(my_y)


C=mse(yhat,y)
print(C)

print(C.backward())
print(m.grad)
print(b.grad)


optimizer=th.optim.SGD([m,b],lr=0.01)
optimizer.step()
print(m)
print(b)
#regression_plot(x,y,m,b)

C=mse(refression(x, m, b),y)
print(C)



epoches=1000
for epoche in range(epoches):
    optimizer.zero_grad()
    yhat = refression(x, m, b)    
    C=mse(yhat,y)
    C.backward()
    optimizer.step()
    
regression_plot(x,y,m,b)    

print(m.item())
print(b.item())