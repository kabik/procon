X = input()
if '.' in X:
    idx = X.index('.')
    print(X[:idx])
else:
    print(X)
