n = int(input())
l = []
for i in range(1,n+1):
    s,p = input().split()
    l.append((s,100-int(p),i))

l.sort()
for item in l:
    print(item[2])
