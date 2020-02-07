a, b = map(int, input().split())
max = max(a,b)
min = min(a,b)

if min < max:
    print(2*max-1)
else:
    print(2*max)
