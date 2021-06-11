# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 13:13:54 2021
qlist.append (q)
    rlist.append (r)
@author: USER
"""
n = int(input('Nを法とする、N='))
i=0
l=0
list=[11,12,],[21,22]
listcopy=[0,0],[0,0]
while(i==2):
    while(l==2):
        listcopy[i][l]=list[i][l]
        l+=1
    i+=1

t=list[0][0]*list[1][1]-list[0][1]*list[1][0]#　　-10
t=t%n#　　N=3で t=2
list1=[0,0],[0,0]
k=t*list[i][l]

list[0][0],list[1][1]=list[1][1],list[0][0]
list[0][1]=-list[0][1]
list[1][0]=-list[1][0]

print(t,k,list)