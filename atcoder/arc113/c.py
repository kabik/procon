S = input()
ans = 0
d = {}
for i in range(1,len(S)-1):
    if S[-i-2] == S[-i-1] != S[-i]:
        ans += i
        if S[-i-2] in d:
            ans -= d[S[-i-2]]
        d = { S[-i-2] : i }
    else:
        if S[-i] in d:
            d[S[-i]] += 1
        else:
            d[S[-i]] = 1
print(ans)
