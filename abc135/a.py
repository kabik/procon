a, b = map(int, input().split())

if int((a+b)/2) == (a+b)/2:
    print(int((a+b)/2))
elif int(-(a+b)/2) == -(a+b)/2:
    print(int(-(a+b)/2))
else:
    print('IMPOSSIBLE')
