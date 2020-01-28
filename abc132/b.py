n = int(input())
p = list(map(int, input().split()))
l = [p[i] for i in range(1,n-1) \
    if p[i+1] < p[i] < p[i-1] or p[i-1] < p[i] < p[i+1]]
print(len(l))
