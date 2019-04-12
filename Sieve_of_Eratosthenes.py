#エラトステネスの篩.N以下の素数を持つ集合を返す

import math
def Sieve_of_Eratosthenes(N):
    prime=set(i for i in range(2,N+1))
    for i in range(2,math.ceil(N**0.5)+1):
        tmp=set()
        for j in prime:
            if j>i and j%i==0: tmp.add(j)
        for j in tmp:
            prime.remove(j)

    return(prime)