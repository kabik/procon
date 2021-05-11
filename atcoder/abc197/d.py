import math

N = int(input())
x0, y0 = map(int, input().split())
xk, yk = map(int, input().split())

qx, qy = (x0+xk)/2, (y0+yk)/2
theta = math.atan2(y0 - qy, x0 - qx)
theta += 2 * math.pi / N
r = math.sqrt( (x0-qx)**2 + (y0-qy)**2 )
x1 = qx + r * math.cos(theta)
y1 = qy + r * math.sin(theta)
print(x1, y1)
