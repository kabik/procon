n = int(input())
p = list(map(int, input().split()))

t = [i for i in range(1,n+1)]
l = [i for i in range(n) if p[i] != t[i]]

if len(l) == 0 or len(l) == 2:
    print('YES')
else:
    print('NO')
