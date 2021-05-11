import math
a,b,x = map(int, input().split())

if x > a*a*b/2:
    theta = math.atan( (2*a*a*b - 2*x) / a**3 )
    print(math.degrees(theta))
else:
    theta = math.atan( a*b*b / (2*x) )
    print(math.degrees(theta))
