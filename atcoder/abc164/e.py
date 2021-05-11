N,M,S = map(int, input().split())
UVAB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(N)]

dp = [[10**20] * (N+1) for _ in range(N+1)]

for t in range(2, N+1):
