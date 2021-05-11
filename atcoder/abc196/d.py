import itertools

H, W, A, B = map(int, input().split())

pat = []
for h in range(H):
    for w in range(W-1):
        pat.append( [W*h+w, W*h+w+1] )
for w in range(W):
    for h in range(H-1):
        pat.append( [W*h+w, W*(h+1)+w] )

ans = 0
C = list( itertools.combinations( pat, A ) )
for c in C:
    l = []
    for a,b in c:
        l.append(a)
        l.append(b)
    s = set(l)
    if len(l) == len(s):
        ans += 1
print(ans)
