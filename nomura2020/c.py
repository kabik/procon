import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

leaf = sum(A)
ans = 0
node = 1
for i in range(N+1):
    if A[i] > node or leaf == 0:
        ans = -1
        break
    ans += node
    leaf -= A[i]
    node = min(2*(node-A[i]), leaf)
print(ans)
