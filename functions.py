"""
return conbination
e.g.
    conb(3, 1) = 3
    conb(6, 2) = 15
"""
def conb(a, b):
    nume = 1
    deno = 1
    for i in range(b):
        nume *= a - i
        deno *= i + 1

    return int(nume / deno)

"""
return gcd
"""
def gcd_step(a, b):
    return b, a % b

def gcd(a, b):
    a, b = gcd_step(a,b)
    while b > 0:
        a,b = gcd_step(a,b)

    return a
