def price(a, b, n):
    return a * n + b * len(str(n))

def middle(l, r):
    return int((r+l)/2)

MAX = 10**9
a,b,x = map(int, input().split())

ans = 0
l,r = 0,MAX
mid = middle(l,r)

if price(a,b,MAX) <= x:
    ans = MAX
    l = r

while l != r:
    pm = price(a,b,mid)
    pm1 = price(a,b,mid+1)
    if pm <= x and pm1 > x:
        ans = mid
        break
    elif pm <= x and pm1 <= x:
        l = mid
    else:
        r = mid
    mid = middle(l,r)

print(ans)
