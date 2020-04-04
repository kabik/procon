N, K, C = map(int, input().split())
S = input()

cand = []
for i in range(1, N+1):
    if S[i-1] == 'o':
        cand.append(i)

print(cand)

pat = {}
for i in range(len(cand)-K+1):
    #pat[i] = [[i]]
    l = [[i]]
    for p in l:
        for j in range(p[-1]+1, len(cand)):
            if p[j]
