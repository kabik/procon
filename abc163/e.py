N = int(input())
A = list(map(int, input().split()))

l = []
for a in reversed(sorted(A)):
    idx = A.index(a)
    A[idx] = -1
    l.append((a,idx))

head, tail = 0, N-1

ans = 0
for tup in l:
    v = tup[0]
    idx = tup[1]

    if abs(idx - head) >= abs(idx - tail):
        ans += v * abs(idx-head)
        head += 1
    else:
        ans += v * abs(idx-tail)
        tail -= 1

print(ans)
