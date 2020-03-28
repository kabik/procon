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
def gcd(a, b):
    while b > 0:
        a,b = b, a%b
    return a
