from itertools import groupby

N, K = map(int, input().split())
S = input()
l = [len([*g]) for _,g in groupby(S)]
L = len(l)

sm = [0]
for k in l:
    sm.append( sm[-1] + k )

ans = 0
if S[0] == '0':
    for i in range(0, L+1, 2):
        ans = max(ans, sm[min(L, i+2*K)] - sm[max(0, i-1)])
else:
    for i in range(1, L+1, 2):
        ans = max(ans, sm[min(L, i+2*K)] - sm[max(0, i-1)])
print(ans)
