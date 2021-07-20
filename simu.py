#一次元配列に値を入れると、暗号化に使う2列の配列に組み替える。
import numpy
a=numpy.array([])
i=0
while(i!=8):
    pre=int(input(F'{i}番目 = '))
    a=numpy.append(a,pre)
    i+=1

#ValueError 検知でループ抜け、奇数なら0？を補い整形したい

b=a.reshape(4,2)
c=b.T
print(a,'\n\n',b,'\n\n',c)

#numpy配列とsympy行列は相容れない？





"""
y=numpy.array([[1,2,3],
    [4,5,6],
    [7,8,9]])

print(y.mean(axis=0),y.var(),y.std(),y.max())#axis=1だと行の平均に

print( "ord({})={}".format( "A", ord( "A" ) ))




number=33
number_bin = bin(number)
print(number_bin)
print(type(number_bin))
 
# format(), str.format()
print(format(number, 'b'))
print('{:b}'.format(number))
 
# ゼロパディング
print('{:08b}'.format(number))
#0b100001
#100001
#100001
#00100001
"""