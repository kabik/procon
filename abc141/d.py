import queue

N, M = map(int, input().split())
A = list(map(int, input().split()))

q = queue.PriorityQueue()
for a in A:
    q.put((-a,a))

for _ in range(M):
    v = q.get()[1] // 2
    q.put((-v, v))

ans = 0
while not q.empty():
    ans += q.get()[1]
print(ans)
