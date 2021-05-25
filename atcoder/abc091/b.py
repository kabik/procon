import collections

N = int(input())
S = [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]

s_ctr = collections.Counter(S)
t_ctr = collections.Counter(T)
ans = 0
for s in s_ctr:
    if s in t_ctr:
        ans = max(ans, s_ctr.get(s) - t_ctr.get(s))
    else:
        ans = max(ans, s_ctr.get(s))
print(ans)
