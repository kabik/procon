# TLE

n, p = map(int, input().split())
s = input()

cnt = 0
for i in range(0, n):
    for j in range(i, n):
        if int(s[i:j+1]) % p == 0:
            cnt += 1

print(cnt)
