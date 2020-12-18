S = input()
T = input()

slen = len(S)
tlen = len(T)
mn = 100000
for i in range(slen-tlen+1):
    cnt = 0
    for j in range(tlen):
        if S[i+j] != T[j]:
            cnt += 1
    mn = min(mn, cnt)
print(mn)
