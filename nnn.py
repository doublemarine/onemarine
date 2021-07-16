# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 22:41:54 2021

@author: USER
"""


import numpy
a=numpy.array([11,52,23,64,15,76,57,8])
b=a.reshape(4,2)
c=b.T
print(a,b,c)

#一次元配列に値を入れると、暗号化に使う2列の配列に組み替える。
#numpy配列はsympy行列と違ってモジュラー逆行列作れない。


#print( "ord({})={}".format( "A", ord( "A" ) ))

y=numpy.array([[1,2,3],
    [4,5,6],
    [7,8,9]])

print(y.mean(axis=0),y.var(),y.std(),y.max())#axis=1だと行の平均に

"""
number=33
number_bin = bin(number)
print(number_bin)
print(type(number_bin))
 
# format(), str.format()
print(format(number, 'b'))
print('{:b}'.format(number))
 
# ゼロパディング
print('{:08b}'.format(number))
#0b100001
#100001
#100001
#00100001
"""