A,B = map(int, input().split())
ans = 'No'
for i in [1,2,3]:
    if A*B*i % 2 == 1:
        ans = 'Yes'
print(ans)
