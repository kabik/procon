A,B,C,X,Y = map(int, input().split())

ans = 10**10
for i in range(max(X,Y)+1):
    x = max(X-i, 0)
    y = max(Y-i, 0)
    cost = x*A + y*B + 2*i*C
    ans = min(ans, cost)
print(ans)
