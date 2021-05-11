n,k = map(int, input().split())
h = list(map(int, input().split()))
h = list(reversed(sorted(h)))
for i in range(k):
    if i > len(h)-1: break
    h[i] = 0

print(sum(h))
