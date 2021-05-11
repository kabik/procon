N = int(input())
X = list(map(int, input().split()))
X = list(map(abs, X))

s = 0
for x in X:
    s += x*x

print(sum(X))
print(s**0.5)
print(max(X))
