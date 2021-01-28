A, B = input().split()

sa = 0
for a in A:
    sa += int(a)

sb = 0
for b in B:
    sb += int(b)

print(max(sa, sb))
