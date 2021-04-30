N = int(input())
D,X = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = X
for a in A:
    for i in range(1, D+1, a):
        ans += 1
print(ans)
