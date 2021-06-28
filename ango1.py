# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 23:38:03 2021

@author: USER
"""

import numpy

a=[[2,3],[1,4]]
b=a
d=[[2,3,5],[3,4,5]]
n=3
c=numpy.dot(a,b)
f=numpy.dot(a,d)
print(c,f)
t=a[0][0]*a[1][1]-a[0][1]*a[1][0]
print(t)
t = t % n
inv=numpy.linalg.inv(a)
a[0][0], a[1][1] = a[1][1], a[0][0]
a[0][1] = -a[0][1]
a[1][0] = -a[1][0]
print(t,inv,a)