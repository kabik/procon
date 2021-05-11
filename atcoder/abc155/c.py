n = int(input())
s = [input() for _ in range(n)]

ans = {}
for t in s:
    if t in ans:
        ans[t] += 1
    else:
        ans[t] = 1

max_cnt = max(ans.values())

for t in sorted(ans):
    if ans[t] == max_cnt:
        print(t)
