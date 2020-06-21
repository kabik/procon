N = int(input())

S = 'zabcdefghijklmnopqrstuvwxy'
l = []
while N > 0:
    k = N % 26
    l.append(S[k])
    N //= 26
    if k == 0:
       N -= 1
l.reverse()
print(''.join(l))
