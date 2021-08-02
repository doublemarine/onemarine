


dic={'A':1,'B':2,'C':3,'D':4,'E':5}
dic.setdefault('F',6)
print(dic,dic.values(),dic.keys())    
print(dic.get('F','値が登録されていません'))
print('key==',list(dic.keys()),'values==',list(dic.values()))
print(list(dic.items()))
dic['E']=dic.get('E',-1)
dic['F']=dic.get('F',-1)
print(dic,'/n')

slice='0123456789'
s01=(slice[1:5])
s02=(slice[1:6:2])
s03=(slice[::-1])
print('slice[配列] a:b:cの時,aからb-1までの範囲を,c-1コの要素を飛ばす')
print(s01,s02,s03,'\n')

ss=[0,1,1,2,0,2]
set=set(ss)
set1={1,2,3,4,5}
set2={3,4,5,6,7}
print(ss,set,'\n積集合->',set1&set2,'和集合->',set1|set2,'差集合->',set1-set2)
moji='apex'
print(type(moji),type(dic),type(set))

listing=[11,2,7,13,5]
print(max(listing),min(listing),sum(listing))
sorted_listing=sorted(listing)#sorted_名前=sorted(名前)　にしないとエラー？？
print(sorted_listing)#降順もできるらしい

