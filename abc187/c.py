N = int(input())
S = [input() for _ in range(N)]

d = {}
for s in S:
    d[s] = True

ans = 'satisfiable'
for s in S:
    if s[0] == '!':
        if s[1:] in d:
            ans = s[1:]
            break
    else:
        if '!' + s in d:
            ans = s
            break
print(ans)
