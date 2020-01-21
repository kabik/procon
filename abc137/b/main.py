k, x = map(int, input().split())

l = []
for i in range(-(k-1), k):
    if -1000000 <= x+i and x+i <= 1000000:
        l.append(x + i)

for i in l:
    print(i, end=" ")
