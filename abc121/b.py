import numpy as np

N, M, C = map(int, input().split())
B = np.array(list(map(int, input().split())))
A = np.array([np.array(list(map(int, input().split()))) for _ in range(N)])

cnt = 0
for a in A:
    if np.sum(a*B) + C > 0: cnt += 1

print(cnt)
