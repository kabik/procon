N = int(input())

sn = 0
for c in str(N):
    sn += int(c)

if N % sn == 0:
    print('Yes')
else:
    print('No')
