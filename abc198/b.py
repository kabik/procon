N = int(input())

ans = 'No'
for i in range(10):
    s = '0'*i + str(N)
    if s == s[::-1]:
        ans = 'Yes'
print(ans)
