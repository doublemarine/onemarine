# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:41:54 2021

@author: USER
"""


import numpy

a=numpy.array([1,2,3,4,5,6,7,8])
b=a.reshape(4,2)
c=b.T
print(a,b,c)

#一次元配列に値を入れると、暗号化に使う2列の配列に組み替える。
#numpy配列はsympy行列と違ってモジュラー逆行列作れない。


print( "ord({})={}".format( "A", ord( "A" ) ))
print( "ord({})={}".format( "a", ord( "a" ) ))
print( "ord({})={}".format( "1", ord( "1" ) ))
#

y=numpy.array([[1,2,3],
    [4,5,6],
    [7,8,9]])

print(y.mean(axis=0),y.var(),y.std(),y.max())#axis=1だと行の平均に
