# ref https://hamukichi.hatenablog.jp/entry/2016/03/30/173446

import sys

# sys.setrecursionlimit(10**6)
input = sys.stdin.buffer.readline
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(input())
def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def LI1(): return list(map(int1, input().split()))
def LLI1(rows_number): return [LI1() for _ in range(rows_number)]
def BI(): return input().rstrip()
def SI(): return input().rstrip().decode()
def LSI(): return SI().split()
def LLSI(rows_number): return [SI() for _ in range(rows_number)]
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353


import array
import collections

Edge = collections.namedtuple("Edge", "start end weight")


class UnionFind(object):

    def __init__(self, number_of_nodes):  # 初期化
        self.par = array.array("L", range(number_of_nodes))
        self.rank = array.array("L", (0 for i in range(number_of_nodes)))

    def root(self, node):  # 根を求める
        if self.par[node] == node:
            return node
        else:
            r = self.root(self.par[node])
            self.par[node] = r  # 経路圧縮
            return r

    def in_the_same_set(self, node1, node2):  # 同じ集合に属するか
        return self.root(node1) == self.root(node2)

    def unite(self, node1, node2):  # 属する集合を併合
        x = self.root(node1)
        y = self.root(node2)
        if x == y:
            pass
        elif self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


# Kruskal法により最小全域木を求める
def compute_mst_kruskal(max_v, edges):
    edges.sort(key=lambda edge: edge.weight)
    uf = UnionFind(max_v)
    mst = []
    ans = sum([edge.weight for edge in edges if edge.weight > 0])
    for edge in edges:
        if edge.weight < 0:
            uf.unite(edge.start, edge.end)
            mst.append(edge)
    for edge in edges:
        if not uf.in_the_same_set(edge.start, edge.end):
            uf.unite(edge.start, edge.end)
            mst.append(edge)
            ans -= edge.weight
    return ans


N, M = LI()
ABC = LLI(M)

max_v, max_e = N,M
edges = [Edge(a-1,b-1,c) for a,b,c in ABC]
print(compute_mst_kruskal(max_v, edges))
