N = int(input())
A = list(map(int, input().split()))

sm = sum(A)
ans = 0
for a in A:
    sm -= a
    ans += (N-1)*a**2 - 2*a*sm
print(ans)
