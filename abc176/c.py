N = int(input())
A = list(map(int, input().split()))

mx = 0
ans = 0
for a in A:
    ans += max(0, mx-a)
    mx = max(a, mx)
print(ans)
