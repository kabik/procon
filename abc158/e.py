N,P = map(int, input().split())
S = input()

if P == 2 or P == 5:
    ans = 0
    for i in range(N):
        if int(S[i]) % P == 0:
            ans += i+1
    print(ans)
else:
    mod_cnt = [0]*P
    mod_cnt[0] = 1
    k = 0.1
    t = 0
    for i in range(1, N+1):
        k = int(k * 10) % P
        t = (t + k * int(S[-i])) % P
        mod_cnt[t] += 1
    ans = 0
    for cnt in mod_cnt:
        ans += (cnt * (cnt-1)) // 2
    print(ans)
