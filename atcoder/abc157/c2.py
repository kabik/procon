N, M = list(map(int, input().split()))
SC = [list(map(int, input().split())) for _ in range(M)]

for i in range(1000):
    i_str = str(i)
    if len(i_str) != N:
        continue
    ok = True
    for s, c in SC:
        if i_str[s-1] != str(c):
            ok = False
    if ok:
        print(i)
        break
else:
    print(-1)
