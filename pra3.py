# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 23:05:24 2021

@author: USER
"""

li = [{'a': 6, 'b': 7, 'c': 6},
      {'a': 4, 'b': 2, 'c': 3},
      {'a': 1, 'b': 5, 'c': 8}]
sorted_li = sorted(li, reverse=True, key=lambda x:x['b'])
print(sorted_li)


li = [5,4,3,2,1]
ans_li = [idx + elem for idx, elem in enumerate(li)]
print(ans_li)

a = 0
b = 5

try:
    print(a / b)
except ZeroDivisionError:
    print('zero division')

try:
    print(b / a)
except ZeroDivisionError:
    print('zero division')
    
dic = {'two':324, 'four':830, 'three':493, 'one':172, 'five':1024}
items_list = list(dic.items())
sorted_items_list = sorted(items_list, key=lambda x:x[1])
ans = [elem[0] for elem in sorted_items_list]
print(ans)