n = int(input())
s = []
t = []

for i in range(0, n):
    si, ti = map(str, input().split())
    s.append( si)
    t.append( int(ti) )

x = input()

sum = 0
sleeping = False
for i in range(0, n):
    if sleeping:
        sum += t[i]
    if s[i] == x:
        sleeping = True

print(sum)
