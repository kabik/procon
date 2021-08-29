X,Y = input().split('.')
Y = int(Y)
if 0 <= Y <= 2:
    print('{}-'.format(X))
elif 3 <= Y <= 6:
    print(X)
else:
    print('{}+'.format(X))
