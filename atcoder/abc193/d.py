K = int(input())
S = input()
T = input()

s_cnt = [0]*10
t_cnt = [0]*10
for i in range(4):
    s_cnt[int(S[i])] += 1
    t_cnt[int(T[i])] += 1

all = 9*K - 2*4
t_win = 0
for i in range(1,10): # s card
    i_rest = K - s_cnt[i] - t_cnt[i]
    if i_rest == 0: continue
    for j in range(1, 10): # t card
        j_rest = K - s_cnt[j] - t_cnt[j]
        if i==j: j_rest-=1
        if j_rest <= 0: continue

        sp = 0
        for k in range(1,10):
            cnt = s_cnt[k]
            if k==i: cnt+=1
            sp += k * 10**cnt

        tp = 0
        for k in range(1,10):
            cnt = t_cnt[k]
            if k==j: cnt+=1
            tp += k * 10**cnt

        if sp > tp:
            t_win += i_rest*j_rest

print(t_win/all/(all-1))
