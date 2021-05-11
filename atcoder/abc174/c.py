K = int(input())

cnt = 0
n = 7
while cnt <= K:
    cnt += 1
    if n % K == 0:
        break
    n = (10 * n + 7) % K

if cnt == K+1:
    print(-1)
else:
    print(cnt)
