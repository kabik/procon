N, K = map(int, input().split())
A = list(map(int, input().split()))

visited = [0] * N
cnt = 0
i = 0
loop = 0
while True:
    visited[i] = cnt
    i = A[i] - 1
    cnt += 1
    if visited[i] > 0 or i == 0:
        loop = cnt - visited[i]
        break

m = 0
if K < visited[i]:
    m = K
    i = 0
else:
    m = (K - visited[i]) % loop

for _ in range(m):
    i = A[i] - 1
print(i+1)
