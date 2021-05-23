# -*- coding: utf-8 -*- 
#Created on Sat May 22 16:37:26 2021 


"""
print('三つの整数の最大値を求めます')
a=int(input('整数 a の値 :'))
b=int(input('整数 b の値 :'))
c=int(input('整数 c の値 :'))
maximum=a
if b >maximum: maximum=b
if c> maximum: maximum=c
print(f'最大値は{maximum}です')#fを入れないと「最大値は{maximum}です」と実行される
t=int('0b11',2)
print(f'{t}  ',t)
"""

def max3(a,b,c):
    maximum=a
    if b >maximum: maximum=b
    if c> maximum: maximum=c
    return maximum
print('run')
