N, W = map(int, input().split())
STP = [list(map(int, input().split())) for _ in range(N)]

MAX = 2*10**5+1
I = [0]*(MAX)

for i in range(N):
    S = STP[i][0]
    T = STP[i][1]
    P = STP[i][2]
    I[S] += P
    I[T] -= P
for i in range(1,MAX):
    I[i] += I[i-1]

ans = True
for i in range(MAX):
    if I[i] > W:
        ans = False
        break

if ans:
    print('Yes')
else:
    print('No')
