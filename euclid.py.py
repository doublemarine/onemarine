# -*- coding: utf-8 -*-
"""
Created on Wed May  5 15:28:22 2021

@author: USER
"""

qlist = []
rlist = []
a = int(input('a='))
b = int(input('b='))
r = a #whileのエラー解消のため、仮の余りを設定する
i = 1

c=a#一時不定方程式を解くときに使いたい。
d=b#GCD算出後に使う為に保存,　ーーーできればリストの中に格納してwhile中に一気に出したい。

while r != 0:
    q = a // b
    r = a % b
    qlist.append (q)
    rlist.append (r)
    print('(',i,')',a,'=',q,'X',b,'+',r)
    a = b
    b = r
    i += 1
print(f'GCD = {a}')