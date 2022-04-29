N = int(input())
C = input()

s = 'ABXY'
ans = 10**9
for i in range(1, 4**4+1):
    j = 0
    cnt = 0
    while j < N:
        c2 = C[j:j+2]
        if c2 == s[(i >> 0) % 4]+s[(i >> 2) % 4] or c2 == s[(i >> 4) % 4]+s[(i >> 6) % 4]:
            j += 2
        else:
            j += 1
        cnt += 1
    ans = min(ans, cnt)
print(ans)
