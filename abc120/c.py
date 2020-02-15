s = input()

cnt = 0
for c in s:
    if c == '0':
        cnt += 1

remove = 2*min(cnt, len(s)-cnt)
print(remove)
