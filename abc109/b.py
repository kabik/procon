N = int(input())
W = [input() for _ in range(N)]
W.append(W[-1][-1])

seen = {}
ans = 'Yes'
for i in range(N):
    if W[i][-1] != W[i+1][0] or W[i] in seen:
        ans = 'No'
        break
    seen[W[i]] = True
print(ans)
