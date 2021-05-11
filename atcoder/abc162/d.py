N = int(input())
S = list(input())

same = 0
for i in range(N):
    for j in range(1, N):
        if i+j*2 > N-1:
            break
        if S[i] != S[i+j] and S[i] != S[i+j*2] and S[i+j] != S[i+j*2]:
            same += 1

cnt = {'R': 0, 'G': 0, 'B': 0}
for c in S:
    cnt[c] += 1

print(cnt['R'] * cnt['G'] * cnt['B'] - same)
