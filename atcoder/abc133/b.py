def distance(x1, x2):
    sum = 0
    for i in range(len(x1)):
        sum += (x1[i] - x2[i])**2
    return sum**(1/2)

n,d = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(len(x)-1):
    for j in range(i+1, len(x)):
        d = distance(x[i], x[j])
        if d == int(d):
            cnt+=1
print(cnt)
