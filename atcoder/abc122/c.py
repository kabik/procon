N,Q = map(int, input().split())
S = input()
LR = [list(map(int, input().split())) for _ in range(Q)]

ac_cnt = [0]
for i in range(1,N):
    ac_cnt.append(ac_cnt[i-1]+1 if S[i-1:i+1] == 'AC' else ac_cnt[i-1])

for lr in LR:
    print(ac_cnt[lr[1]-1] - ac_cnt[lr[0]-1])
