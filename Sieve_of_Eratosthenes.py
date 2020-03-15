#エラトステネスの篩.N以下の素数を持つ集合を返す

import math
def Sieve_of_Eratosthenes(N):
    if N<2: return set()
    prime=set(i for i in range(2,N+1))
    for i in range(2,math.ceil(N**0.5)+1):
        tmp=set()
        for j in prime:
            if j>i and j%i==0: tmp.add(j)
        for j in tmp:
            prime.remove(j)

    return prime

#リスト版、こっちの方が高速。
def Sieve_of_Eratosthenes(N):
    if N<2:
        prime = [False for i in range(N+1)]
        return prime
 
    prime = [True for i in range(N+1)]
    prime[0] = False
    prime[1] = False
 
    for i in range(2, int(N**0.5)+1):
        if prime[i]:
            for j in range(i*2, N+1, i):
                prime[j] = False
 
    return prime
