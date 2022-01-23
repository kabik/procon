from heapq import heappush, heappushpop

N, K = list(map(int, input().split()))
P = list(map(int, input().split()))

q = []
for p in P[:K-1]:
    heappush(q, p)

pre = -1
for i in range(K-1, N):
    x = heappushpop(q, P[i])
    if pre <= x:
        print(x)
        pre = x
    else:
        print(pre)
