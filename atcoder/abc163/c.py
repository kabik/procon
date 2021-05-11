N = int(input())
A = list(map(int, input().split()))

l = {}
for a in A:
    if a in l:
        l[a] += 1
    else:
        l[a] = 1

for i in range(1, N+1):
    if i in l:
        print(l[i])
    else:
        print(0)
