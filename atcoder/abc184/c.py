r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r = r2 - r1
c = c2 - c1
if (r,c) == (0,0):
    print(0)
elif r == c or r == -c:
    print(1)
elif abs(r) + abs(c) <= 3:
    print(1)
elif (r ^ c ^ 1) & 1:
    print(2)
elif abs(r) + abs(c) <= 6:
    print(2)
elif abs(r + c) <= 3 or abs(r - c) <= 3:
    print(2)
else:
    print(3)
