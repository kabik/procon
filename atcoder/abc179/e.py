N, X, M = map(int, input().split())

L = [-1]*(M)
loop_start = X
while L[loop_start] < 0:
    L[loop_start] = loop_start**2%M
    loop_start = L[loop_start]

cnt_in_loop = 1
sum_in_loop = loop_start
k = L[loop_start]
while k != loop_start:
    cnt_in_loop += 1
    sum_in_loop += k
    k = L[k]

ans = 0
k = X
cnt_before_loop = 0
for _ in range(N):
    cnt_before_loop += 1
    ans += k
    k = L[k]
    if k == loop_start:
        break

if cnt_before_loop < N:
    k = loop_start
    for _ in range( (N-cnt_before_loop-1)%cnt_in_loop+1 ):
        ans += k
        k = L[k]

if cnt_before_loop < N:
    ans += sum_in_loop * ((N - cnt_before_loop - 1) // cnt_in_loop)
print(ans)
