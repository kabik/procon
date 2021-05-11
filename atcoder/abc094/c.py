N = int(input())
X = list(map(int, input().split()))
Y = sorted(X)

for i in range(N):
    if X[i] <= Y[N//2-1]:
        print(Y[N//2])
    else:
        print(Y[N//2-1])
