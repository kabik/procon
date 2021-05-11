N = int(input())
P = [int(input()) for _ in range(N)]

ans = sum(P) - max(P)//2
print(ans)
