# N: list size
# A: list
#

N = 3
A = [1,2,3]

def bottom_size(n):
    size = 1
    while True:
        if N // size == 0:
            return size
        size *= 2

def update(i, x):
    i += M-1
    seg_tree[i] = x
    while i > 0:
        i = (i-1)//2
        seg_tree[i] = seg_tree[i*2+1] ^ seg_tree[i*2+2]
        # seg_tree[i] = min(seg_tree[i*2+1], seg_tree[i*2+2])

def init(A):
    for i, a in enumerate(A):
        update(i, a)

def query(a, b, k, l, r):
    if r <= a or b <= l:
        return 0
    elif a <= l and r <= b:
        return seg_tree[k]
    else:
        vl = query(a, b, k*2+1, l, (l+r)//2)
        vr = query(a, b, k*2+2, (l+r)//2, r)
        return vl ^ vr
        # return min(vl, vr)

M = bottom_size(N)
seg_tree = [0]*(M*2 - 1)
init(A)
