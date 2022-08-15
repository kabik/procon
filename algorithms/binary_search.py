# 二分探索
# O(log n)
def some_condition(x):
    return x < 10**20

def binary_search():
    ng, ok = -1, 10**40
    while ok-ng > 1:
        m = (ng + ok) // 2
        if some_condition(m):
            ng = m
        else:
            ok = m
    return ok
