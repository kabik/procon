n,k = map(int, input().split())
p = list(map(int, input().split()))

ex_pre = 0
for i in range(k):
    ex_pre += (p[i]+1)/2

ex_max = ex_pre
for i in range(k, n):
    ex = ex_pre + (p[i]+1)/2 - (p[i-k]+1)/2
    ex_max = max(ex, ex_max)
    ex_pre = ex

print(ex_max)
