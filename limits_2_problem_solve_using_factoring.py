# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 15:42:38 2021

@author: Mahfuz_Shazol
"""



# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 02:15:18 2021

@author: Mahfuz_Shazol
"""

import numpy as np
import matplotlib.pyplot as plt

#limit x->1=(x^2-1)/(x-1)
x=np.linspace(-10,10,1000)

def calculate_limit(x):
    x=x+1
    return x


y=calculate_limit(x)

fig,ax=plt.subplots()

plt.axvline(x=0,color='lightgray')
plt.axhline(y=0,color='lightgray')

plt.xlim(-1,5)
plt.ylim(-1,5)

plt.axvline(x=1,color='purple',linestyle='--')
plt.axhline(y=2,color='purple',linestyle='--')

_ =ax.plot(x,y)


