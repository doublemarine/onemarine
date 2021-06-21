# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 17:55:55 2021

@author: USER
"""
import sys

i=0
n = int(input('n='))
a = 0
b = 0
q = []

while(1):
    b = int(input('暗号化したい　n進数の　数列を　後ろから入力 | '))
    if b ==-1:
        break
    elif b >= n:
        print('この数字の　入力のみ　やり直す -> 0\n終了する /　やり直す -> 1')
        z=int(input())
        if z==0 :
            print('\n-------\n現在の入力状況　>>> ',q)
            continue
        else:
            sys.exit(1)
    a = a+b*(n**i)
    q.append(b)
    i+=1
print('\n  ',a)

#a = int(input(''))
#大きいほうから入力できるようにしたい　　→　　リスト逆順に、-1はどうしよう？？
#計算して出た１０進数の暗号をリストに格納したい
#そんなことより　　暗号化プログラム作らなきゃ