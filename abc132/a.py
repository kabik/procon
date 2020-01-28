s = input()

d = {}
for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 0

if len(d) == 2:
    print('Yes')
else:
    print('No')
