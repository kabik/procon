from collections import Counter

N = int(input())
S = input()
ans = 0
for i in range(N):
    c1 = Counter(S[:i])
    c2 = Counter(S[i:])
    cnt = 0
    for k in c1:
        if k in c2:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
