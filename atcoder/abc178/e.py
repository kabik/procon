import sys
input = sys.stdin.readline

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

max_z = max_w = -10**10
min_z = min_w = 10**10
for x,y in XY:
    z, w = x+y, x-y
    max_z = max(max_z, z)
    min_z = min(min_z, z)
    max_w = max(max_w, w)
    min_w = min(min_w, w)
print( max( max_z-min_z, max_w-min_w))
