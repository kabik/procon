N, X = map(int, input().split())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

s = []
for c in alphabet:
    for i in range(N):
        s.append(c)
print(s[X-1])
