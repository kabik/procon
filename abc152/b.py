a, b = map(int, input().split())

s = ''
for i in range(a):
    s = s + str(b)

t = ''
for i in range(b):
    t = t + str(a)

l = [s, t]
l.sort()
print(l[0])
