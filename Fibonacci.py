# Fibonacci数列を求める関数
# F_0=0,F_1=1,F_2=1,F_3=2,F_4=3… という仕様

def fibonacci_sub(n,last1,last2):
    if n==0:
        return last2
    else:
        return fibonacci_sub(n-1,last1+last2,last1)




def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci_sub(n,1,0)