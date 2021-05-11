S = input()
N = len(S)

ans = [0] * N
r_num = 0
r_idx, l_idx = -1, -1
for i in range(N-1):
    if S[i:i+2] == 'RL':
        r_idx = i
        l_idx = i+1
        ans[r_idx] += r_num//2 + 1
        ans[l_idx] += r_num//2 + 1
        if r_num % 2 == 1:
            ans[l_idx] += 1
        r_num = 0
    elif S[i] == 'R':
        r_num += 1
    elif S[i-1:i+1] != 'RL':
        if (i - r_idx) % 2 == 0:
            ans[r_idx] += 1
        else:
            ans[l_idx] += 1
if S[N-2:N] != 'RL':
    if (N-1 - r_idx) % 2 == 0:
        ans[r_idx] += 1
    else:
        ans[l_idx] += 1

for i in range(N):
    print(ans[i], end=' ')
print()
