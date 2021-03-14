N = int(input())
ans = 0
for i in range(1,10):
    ans += max(N-1000**i+1,0)
print(ans)
