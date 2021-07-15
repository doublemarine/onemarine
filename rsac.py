# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 22:33:25 2021

@author: USER
"""

#ifの部分はいずれ関数化したい　+文字を数値にはどうしてもできないから、せめて基数変換くらいやりたい
import numpy
import sympy

swith = int(input(' 暗号化 -> 0  /  復号化 or 電子署名 -> 1  /  素因数分解 -> 2 \n'))
if swith ==0:
    P = int(input('平文を数値化した値 = '))
    n = int(input('n='))#1219,263
    e = int(input('e='))  # 476
    
    print((P**e) % n, '\n')  # 105

elif swith ==1:
    p = int(input('p='))
    q = int(input('q='))
    n = p*q
    L = (numpy.lcm(p-1, q-1))
    print('最小公倍数 L =',L)
    e = int(input('e='))
    d,y,z=sympy.gcdex(e,L)
    d=d%L #dを最小生剰余に
    print('最小公倍数 L =',L,'  /  復号化鍵(署名用暗号化鍵) d　=',d)
    C=int(input('暗号文(署名前の文)を数値化した値 = '))
    P=(C**d)%n
    #P=pow(C,d,n)# unsupported operand type(s) for pow(): 'int', 'Integer', 'int'
    print(P,'元の文（署名済みの文） を数値化した値')
elif swith ==2:
    n = int(input('n='))
    list=[]
    for i in range(2,n+1):
        while True:
            if n%i == 0:
                list.append(i) # 余り0なら素因数分解リストにappendする
                n = n//i # nの更新
                print(list)
                print("n={}".format(n)) # nの更新状況をみてみる
            else:
                    break

    
else :
    print("想定されていない入力です")