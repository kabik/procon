N = int(input())
A = list(map(int, input().split()))

i = 1
for a in A:
    if a == i:
        i += 1

if i == 1:
    print(-1)
else:
    print(N-i+1)
