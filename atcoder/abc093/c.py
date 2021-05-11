L = list(map(int, input().split()))

ans = 0
while len(set(L)) > 1:
    L.sort()
    if L[0] == L[1]:
        L[0] += 1
        L[1] += 1
    else:
        L[0] += 2
    ans += 1
print(ans)
