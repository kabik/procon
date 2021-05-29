S = input()

ans = 0
for i in range(0, 10000):
    i_str = str(i).zfill(4)

    ok = True
    for j in i_str:
        if S[int(j)] == 'x':
            ok = False
    for ci in range(10):
        if S[ci] == 'o' and str(ci) not in i_str:
            ok = False
    if ok:
        ans += 1
print(ans)
