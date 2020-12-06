import itertools

N = input()
ans = -1
for i in range(1, len(N)+1):
    for v in itertools.combinations(N, i):
        s = 0
        for k in v:
            s += int(k)
        if s % 3 == 0:
            ans = len(N) - i
print(ans)
