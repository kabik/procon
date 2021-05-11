T = int(input())

ans = []
for _ in range(T):
    l, r = map(int, input().split())
    n = r-l-l+1
    if l == r == 0:
        print(1)
    elif l == r:
        print(0)
    elif r-l < l:
        print(0)
    else:
        print(n*(n+1)//2)
print('\n'.join(map(str, ans)))
