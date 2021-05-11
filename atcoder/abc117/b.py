N = int(input())
L = list(map(int, input().split()))

sm = sum(L)
mx = max(L)

if mx < sm - mx:
    print('Yes')
else:
    print('No')
