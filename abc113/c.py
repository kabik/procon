N, M = map(int, input().split())
PY = [list(map(int, input().split())) for _ in range(M)]

py_sorted = sorted(PY)
d = {}
now_p = 0
cnt = 1
for p,y in py_sorted:
    if p != now_p:
        cnt = 1
        now_p = p
    else:
        cnt += 1
    d[(p,y)] = cnt

for p,y in PY:
    p_num = str(p).zfill(6)
    y_num = str(d[(p,y)]).zfill(6)
    print(p_num+y_num)
