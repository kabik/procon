import math
N = int(input())

def f(x, y, z):
    return x*x + y*y + z*z + x*y + y*z + z*x

ans = [0] * (N+1)
for x in range(1, math.ceil(N**0.5)):
    for y in range(x, math.ceil(N**0.5)):
        for z in range(y, math.ceil(N**0.5)):
            k = f(x,y,z)
            if k <= N:
                if x == y == z:
                    ans[k] += 1
                elif x == y or y == z or z == x:
                    ans[k] += 3
                else:
                    ans[k] += 6
for i in range(1, N+1):
    print(ans[i])
