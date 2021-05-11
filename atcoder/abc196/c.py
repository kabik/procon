N = int(input())

ans = 0
for i in range(1, int(N**0.5)+1):
    if int( str(i)+str(i) ) <= N:
        ans += 1
    else:
        break
print(ans)
