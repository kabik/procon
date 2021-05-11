import itertools

N, M, Q = map(int, input().split())
abcds = [list(map(int, input().split())) for _ in range(Q)]

As = list(itertools.combinations_with_replacement(range(1,M+1),N))

ans = 0
for A in As:
    sm = 0
    for abcd in abcds:
        a, b, c, d = abcd[0], abcd[1], abcd[2], abcd[3]
        if A[b-1] - A[a-1] == c:
            sm += d
    ans = max(ans, sm)
print(ans)
