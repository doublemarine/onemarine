"""
D=(a*d-b*c)%mod
x,y,z=sympy.gcdex(D,mod)
x=x%mod
print(x)
P=sympy.Matrix([[3,7,4],[9,2,6]])

"""

import sympy

def main():
    switch=input('暗号化鍵で暗号化 -> 1  /  暗号化鍵で複合化 -> 2  /  鍵解読 (2x2の暗号文と平文が必要) -> 3')
    if switch == '1':
        key,mod=setting()
        print('')
    elif switch == '2':
        print('暗号文')
    elif switch == '3':
        print('暗号文')
    else :
        print('')

def setting():
    
    print('[[a,b],[c,d]](mod n)')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    d=int(input('d='))
    mod=int(input('mod='))
    k=sympy.Matrix([[a,b],[c,d]])
    return k,mod


def decrypt():
    k_inv=k.inv_mod(mod)#何故かこれは正常に動く。
    print(k)
    C=k_inv*P
    print(C)


if __name__ == '__main__':
    main()