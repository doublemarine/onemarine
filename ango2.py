# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 18:54:28 2021

@author: USER
"""

#ifの部分はいずれ関数化したい　+文字を数値にはどうしてもできないから、せめて基数変換くらいやりたい
import numpy
import sympy

swith = int(input(' encrypto -> 0 /n decrypto -> other '))
if swith ==0:
    n=0
    n = int(input('n='))#1219,263
    e = int(input('e='))  # 476
    P = int(input('平文を数値化した値 = '))
    print((P**e) % n, '\n')  # 105

else:
    p = int(input('p='))
    q = int(input('q='))
    n = p*q
    L = (numpy.lcm(p-1, q-1))
    d,y,z=sympy.gcdex(e,L)
    while(d < 0):
        d=d+e
        print('最小公倍数 L =',L,'/n復号化鍵 d　=',d)
        C=int(input('暗号文を数値化した値 = '))
        print((C**d) % n)