N, K = map(int, input().split())
S = input()

happy = 0
for i in range(N-1):
    if S[i] == S[i+1]:
        happy += 1

m = 0
for i in range(N-1):
    if S[i] == 'R' and S[i+1] == 'L':
        m += 1

if K <= m:
    happy += 2*K
else:
    if m > 1:
        happy += 2*m
    if S[0] != S[N-1]:
        happy += 1
print(happy)
