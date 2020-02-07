s = list(input())

cnt = 0
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        s[i] = '0' if s[i-1] == '1' else '1'
        cnt += 1

print(cnt)
