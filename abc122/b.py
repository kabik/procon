s = input()
m = 0
cnt = 0
for c in s:
    if c in 'ACGT':
        cnt += 1
        m = max(cnt, m)
    else:
        cnt = 0
print(m)
