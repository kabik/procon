n,l = map(int, input().split())
sum_n = n * (l-1) + (n * (n+1)) // 2

min = 10**9
ind = -1
for i in range(1,n+1):
    diff = abs(l+i-1)
    if diff < min:
        min = diff
        ind = i

print(sum_n - (l+ind-1))
