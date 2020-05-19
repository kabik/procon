import queue

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

nexts = [[] for _ in range(N+1)]

for ab in AB:
    a,b = ab[0], ab[1]
    nexts[a].append(b)
    nexts[b].append(a)

ans = [0] * (N+1)

q = queue.Queue()
q.put(1)
while q.qsize() > 0:
    k = q.get()
    for i in nexts[k]:
        if ans[i] == 0:
            q.put(i)
            ans[i] = k

print('Yes')
for i in range(2,N+1):
    print(ans[i])
