S = input()
T = input()

N = len(S)
sd,td = {},{}
ans = 'Yes'
for i in range(N):
    if S[i] in td:
        if td[S[i]] != T[i]:
            ans = 'No'
            break
    else:
        td[S[i]] = T[i]

    if T[i] in sd:
        if sd[T[i]] != S[i]:
            ans = 'No'
            break
    else:
        sd[T[i]] = S[i]
print(ans)
