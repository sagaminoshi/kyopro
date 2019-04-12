#参考: http://at274.hatenablog.com/entry/2018/02/02/173000#Union-Find%E6%9C%A8%E3%81%AE%E6%A9%9F%E8%83%BD%E3%81%A8%E5%AE%9F%E8%A3%85
# 頂点番号として1,2,…nを用いる。0は使わない

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)