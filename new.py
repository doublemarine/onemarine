# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 11:16:35 2021

@author: USER やること、平文が2x2だとは限らない場合の入力、プリントのフォーマットとかいうやつ

"""

import numpy as nm
import sympy

def main():
    a,b=gcdex1()
    li1=nm.array([[1,2],[3,4]])
    li2=nm.mod(li1,2)
    li3=nm.dot(li1,li2)
    li4=nm.dot(li2,li1)
    print(li1,'\n\n',li2,'\n')
    print(li3,'\n\n',li4,'\n')
    
    
    li1_inv=nm.linalg.inv(li1)
    print(li1_inv)
    
    n=3
    li6=nm.linalg.inv_mod(li1,n)
    
    print(li6)

def gcdex1():
    
    e=43
    L=112
    d,y,z=sympy.gcdex(e,L)
    #print(d,y,z)
    return e,L


if __name__=="__main__":
    main()


