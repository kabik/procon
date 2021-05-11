N, X = map(int, input().split())
M = [int(input()) for _ in range(N)]
M.sort()

ans = N
X -= sum(M)
ans += X // M[0]
print(ans)
