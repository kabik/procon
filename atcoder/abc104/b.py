from collections import Counter

S = input()
ans = 'WA'

ctr = Counter(S[2:-1])
if S[0] == 'A' and ctr['C'] == 1:
    cnt = 0
    for c in S[1:]:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            cnt += 1
    if cnt == 1:
        ans = 'AC'
print(ans)
