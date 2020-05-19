N = int(input())

d = N % 10
if d in [2,4,5,7,9]:
    print('hon')
elif d in [0, 1, 6, 8]:
    print('pon')
else:
    print('bon')
