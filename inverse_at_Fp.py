#拡張ユークリッドの互除法で有限体F_pにおける逆元を求める
# 参考:
# http://taichino.com/programming/2628

# https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
# https://qiita.com/drken/items/b97ff231e43bce50199a


# egcdは拡張ユークリッドの互除法パート
# a*lastx+b*lasty=gca(a,b)をみたす(lastx,lasty,a)を返す
def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)

# ax ≡ 1 (mod m)なるxを返す
def modinv(a, m):
    (inv, q, gcd_val) = egcd(a, m)
    return inv % m

#簡易版
def inv(a,m):
    b=m
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return lastx % m
