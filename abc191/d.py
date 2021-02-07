import math

X,Y,R = map(float, input().split())
D = 10**4
X = round(X * D)
Y = round(Y * D)
R = round(R * D)

ans = 0
start = (X-R)//D
end   = (X+R)//D
for x in range(start, end+1):
    t = pow(R, 2) - pow(X-x*D, 2)
    if t >= 0:
        t_sq = math.isqrt(t)
        y_max = int((Y + t_sq)    // D)
        y_min = int((Y - t_sq -1) // D)
        ans += y_max - y_min
print(ans)
