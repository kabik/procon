A,B,C,D = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a,b = b, a%b
    return a

def count(n):
    c = n//C
    d = n//D
    g = gcd(C, D)
    l = C*D//g
    return n -c -d +n//l

print(count(B) - count(A-1))
