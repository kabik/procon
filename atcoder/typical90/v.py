import math
a,b,c = list(map(int, input().split()))
g = math.gcd(a,b)
g = math.gcd(g,c)
print((a+b+c)//g-3)
