N,K = map(int, input().split())

dic = {}
for i in range(K):
    _ = int(input())
    A = list(map(int, input().split()))
    for a in A:
        if not a in dic:
            dic[a] = 1

ans = 0
for i in range(1, N+1):
    if not i in dic:
        ans += 1
print(ans)
