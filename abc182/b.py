N = int(input())
A = list(map(int, input().split()))

ans = 2
gcd_max = 0
for i in range(2, max(A)+1):
    cnt = 0
    for a in A:
        if a % i == 0:
            cnt += 1
    if cnt > gcd_max:
        ans = i
        gcd_max = cnt
print(ans)
