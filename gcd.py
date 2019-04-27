#python3.4以前のmathには無いので

def gcd(a,b):
    if b>a:
        a,b=b,a
    while b:
        a,b=b, a%b
    return a
