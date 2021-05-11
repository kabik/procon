import queue
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
AB = []
for _ in range(N):
    ab = list(map(int, input().split()))
    a,b = ab[0], ab[1]
    AB.append((a,b))
AB.sort()

q = queue.PriorityQueue()
idx = 0
ans = 0
for i in range(1, M+1):
    while True:
        if idx >= N or AB[idx][0] > i:
            break
        b = AB[idx][1]
        q.put((-b, b))
        idx += 1
    if not q.empty():
        ans += q.get()[1]
print(ans)
