N = int(input())
XYH = [list(map(int, input().split())) for _ in range(N)]

for cx in range(101):
    for cy in range(101):
        h_list = []
        ok = True
        for x,y,h in XYH:
            if h == 0: continue
            h_list.append(h + abs(cx - x) + abs(cy - y))
        if len(list(set(h_list))) == 1:
            ch = h_list[0]
            ok = True
            for x,y,h in XYH:
                if h != max(ch - abs(cx-x) - abs(cy-y), 0):
                    ok = False
            if ok:
                ans = [cx,cy,h_list[0]]
print(ans[0], ans[1], ans[2])
