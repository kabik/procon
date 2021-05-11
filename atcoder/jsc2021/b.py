from collections import Counter

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt_a = Counter(A)
cnt_b = Counter(B)
ans = []

for a in cnt_a:
    if a not in cnt_b:
        ans.append(a)

for b in cnt_b:
    if b not in cnt_a:
        ans.append(b)

ans.sort()
for x in ans:
    print(x, end=' ')
