# see https://hamukichi.hatenablog.jp/entry/2016/03/30/173446

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
    for edge in edges:
        if not uf.in_the_same_set(edge.start, edge.end):
            uf.unite(edge.start, edge.end)
            mst.append(edge)
    return mst


def main():
    max_v, max_e = map(int, input().split())
    edges = [Edge(*map(int, input().split())) for _ in range(max_e)]
    mst = compute_mst_kruskal(max_v, edges)
    print(sum(edge.weight for edge in mst))


if __name__ == '__main__':
    main()
