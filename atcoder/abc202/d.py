A,B,K = map(int, input().split())

def fac(an,bn):
    r = 1
    for i in range(1,an+bn+1):
        r *= i
    for i in range(1,an+1):
        r //= i
    for i in range(1,bn+1):
        r //= i
    return r

def fun1(an, bn, k):
    if an == bn == 0:
        return ''
    pat = fac(an-1,bn)
    if an == 0:
        return 'b' + fun1(an, bn-1, k-pat)
    elif bn == 0:
        return 'a' + fun1(an-1, bn, k)
    elif k <= pat:
        return 'a' + fun1(an-1, bn, k)
    else:
        return 'b' + fun1(an, bn-1, k-pat)

print(fun1(A,B,K))
