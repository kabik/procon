X,Y = map(int, input().split())
if min(X,Y) + 3 > max(X,Y):
    print('Yes')
else:
    print('No')
