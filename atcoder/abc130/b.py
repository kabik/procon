n,x = map(int, input().split())
l = list(map(int, input().split()))

d = 0
cnt = 1
for i in range(1,n+1):
    d += l[i-1]
    if d <= x: cnt += 1

print(cnt)
