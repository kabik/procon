from itertools import product

N = int(input())
A = list(map(int, input().split()))

PAT = list( product([0,1], repeat=N) )

ans = 2**30
for pat in PAT:
    sets = [[ A[0] ]]
    for i in range(1, N):
        if pat[i]:
            sets.append([])
        sets[-1].append(A[i])

    xor = 0
    for s in sets:
        k = 0
        for a in s:
            k |= a
        xor ^= k
    ans = min(ans, xor)
print(ans)
