# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 23:53:51 2021

@author: Mahfuz_Shazol
"""

import tensorflow as tf


x=tf.Variable(5.0)

with tf.GradientTape() as t:
     t.watch(x) #forward pass
     y=x**2
     
result=t.gradient(y,x)    

print(result)