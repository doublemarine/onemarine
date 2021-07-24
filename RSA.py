#40917=漢字最後12345678912345678912345678912345678923456789
#import sympy

def main():
    switch = int(input(' 暗号化 -> 1  /  復号化 or 電子署名 -> 2  /  素因数分解 -> 3 \n ==>>'))
    if switch ==1:
        setting()
        print('')
    elif switch == 2:
        crypt()
    elif switch == 3:
        reading()
        print('暗号文')
    else :
        print('')

def setting():
    p1=str(input('暗号化する文章を入力\n->'))
    ii=1
    e=int(input('公開鍵 e を入力'))#互いに素である二つの数の積
    mod=int(input('公開鍵 mod (n) を入力'))#モジュロ演算に用いる数
    P=0
    for i in p1:
        ins=ord(i)
        plen=len(p1)-ii
        print(type(plen))
        ii+=1
        ins=ins*(40917**plen)
        print(type(plen))
        P=P+ins
    print(P,pow(P,e,mod))



def crypt():
    P=int(input('=='))
    p2=[]
    while(1):
        P=P//40917
        ins1=P%40917
        if P!=0:
            ins1=chr(ins1)#未登録の数字が出てしまうと表記がおかしくなる。一応戻せる。
            p2.insert(0, ins1)
        else:
            break
    print(P,p2)
    

"""

def setting():
    P0=str(input('暗号化する「小文字のアルファベットの」文章を入力\n->'))
    p_l=len(P0)
    P1=([])
    print(p_l,type(P0))
    for p in P0:
        ins1=P0[p]
        ins2=ord(ins1)
        P1.append(ins2)

"""

def reading():
    print('a')
    

if __name__ == '__main__':
    main()