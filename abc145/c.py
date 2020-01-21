import itertools
import math

def dist(x1, x2, y1, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def dist_p(p1, p2):
    return dist(p1[0], p2[0], p1[1], p2[1])

n = int(input())
c = []

for i in range(n):
    xi,yi = map(int, input().split())
    c.append((xi, yi))

l = list(itertools.permutations(c))

sum = 0
for e in l:
    for i in range( len(e)-1 ):
        sum += dist_p(e[i], e[i+1])

print(sum/len(l))
