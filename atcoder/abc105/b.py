N = int(input())
ans = 'No'
for i in range(30):
    for j in range(30):
        if 4*i + 7*j == N:
            ans = 'Yes'
print(ans)
