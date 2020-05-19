import math

A, B, H, M = map(int, input().split())

angle = 30*H + M*0.5 - M*6
rad = math.radians(angle)
print( (A*A + B*B - 2*A*B*math.cos(rad)) **0.5 )
