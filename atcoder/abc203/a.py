a,b,c = map(int, input().split())
l = sorted([a,b,c])
if l[0] == l[1]:
    print(l[2])
elif l[1] == l[2]:
    print(l[0])
else:
    print(0)
