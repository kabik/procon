N = int(input())
S = [input() for _ in range(N)]

ans = 1
for i in range(N):
    if S[i] == 'OR':
        ans += 2**(i+1)
print(ans)
