a,b,c,d = map(int, input().split())
ans = 'No'
if abs(a-c) <= d:
    ans = 'Yes'
elif abs(a-b) <= d and abs(b-c) <= d:
    ans = 'Yes'
print(ans)
