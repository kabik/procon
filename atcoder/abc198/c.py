import math

R,X,Y = map(int, input().split())
d = math.sqrt(X**2 + Y**2)
if d == R:
    print(1)
elif d <= 2*R:
    print(2)
else:
    print( math.ceil( d / R) )
