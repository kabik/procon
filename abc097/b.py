X = int(input())
ans = 1
for i in range(1, X):
    for j in range(2, 1000):
        if i**j > X:
            break
        ans = max(ans, i**j)
print(ans)
