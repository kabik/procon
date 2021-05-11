X = input()
M = int(input())

d = 0
for c in X:
    d = max(d, int(c))

LEN = len(X)
if LEN == 1:
    if int(X) <= M:
        print(1)
    else:
        print(0)
else:
    bt,up = d+1, M+1
    while bt < up:
        mid = (bt+up)//2
        num,k = 0, 1
        for i in range(LEN):
            num += int(X[-i-1])*k
            k *= mid
        if num > M:
            up = mid
        else:
            bt = mid+1
    ans = max(0, (bt+up)//2 -d -1)
    print(ans)
