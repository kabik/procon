N, M = map(int, input().split())
A = list(reversed(sorted(list(map(int, input().split())))))

sm = sum(A)
ans = 'Yes'
for i in range(M):
    if A[i] < sm / (4*M):
        ans = 'No'

print(ans)
