N = int(input())
A = list(map(int, input().split()))

d = {}
for a in A:
    d[a] = True
ans = 0
for x in d:
    sm = 0
    for a in A:
        if a < x:
            ans = max(sm, ans)
            sm = 0
        else:
            sm += x
    ans = max(sm, ans)
print(ans)
