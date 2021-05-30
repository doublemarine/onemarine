# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

x = 20
a = 12
a, x = x, a
print(a, x, '  ', a+x, a-x, a*x, a/x, a//x, a % x)
b = 2
y = 3
print('--------\n', b**y)
if a > b:
    print('aの方が大きい')
elif a == b:
    print('bの方が大きい')
else:
    print('aとbは同じ値')
t = 'python'
s1 = 'py'
s2 = 'thon'
print('\n', t[2], t[5], s1+s2)
a = 5
b = 3
ans = "{}%{}={}".format(a, b, a % b)
print('  ',ans,'\n')
s='SOME1'
s=s.replace('1','one')
print(s)
s=s.lower()
print(s)
s=s.upper()
s3='34'
s4='43'
print(len(s),int(s3)+int(s4),'文字を数値に')


print('-------')
list1=[1,2,3]
list2=[4,5]
list1.extend(list2)
list1.append(6)
list1.insert(0,100)
if 100 in list1:
    print('100がリスト内に存在する')
print(list1,list1[3],len(list1))
list=[1,2,3,4,5]
for tsil in list:
    if tsil % 2 ==0:        
        print(tsil,enumerate(list))