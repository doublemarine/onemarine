# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 11:16:35 2021

@author: USER やること、平文が2x2だとは限らない場合の入力、プリントのフォーマットとかいうやつ

何も起こらない？？？？？！！！！！
"""

import numpy as nm
import sympy

def main():
    a,b=gcdex1()
    li1=nm.array([[1,2],[3,4]])
    li2=nm.mod(li1,2)
    print(li1,li2)

def gcdex1():
    
    e=43
    L=112
    d,y,z=sympy.gcdex(e,L)
    #print(d,y,z)
    return e,L

"""
if __name__=="__main__":
    main()
"""