def dudge(k):
    for i in range(n):
        p = (k >> i) % 2
        if p == 0: continue

        for claim in xy[i]:
            x = claim[0]
            y = claim[1]

            truth = (k >> x-1) % 2
            if truth == 1 and y == 0:
                return False
            elif truth == 0 and y == 1:
                return False
    return True


n = int(input())

xy = []
for i1 in range(n):
    ai = int(input())
    xy.append([])

    for i2 in range(ai):
        xi,yi = map(int, input().split())
        xy[i1].append((xi, yi))

result = 0
for k in range(1 << n):
    if dudge(k):
        l = [i for i in range(n) if (k >> i) % 2 == 1]
        cnt = 0
        result = max(result, len(l))

print(result)
