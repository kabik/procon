S = int(input())
MAX = 1000001

ans = 0
d = [False]*MAX
m = S
for i in range(MAX):
    if d[m]:
        ans = i+1
        break
    d[m] = True
    if m & 1:
        m = 3*m+1
    else:
        m = m//2
print(ans)
