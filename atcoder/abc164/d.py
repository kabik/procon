S = input()
N = len(S)

MOD = 2019
mod_cnt = [0]*MOD
mod_cnt[0] = 1
k = 0.1
t = 0
for i in range(1, N+1):
    k = int(k * 10) % MOD
    t = (t + k * int(S[-i])) % MOD
    mod_cnt[t] += 1
ans = 0
for cnt in mod_cnt:
    ans += (cnt * (cnt-1)) // 2
print(ans)
