A,B = map(int, input().split())

if A & 1 == 1 and B & 1 == 1:
    n = (B-A)//2
    print(A^(n&1))
elif A & 1 == 0 and B & 1 == 0:
    n = (B-A)//2
    print(B^(n&1))
elif A & 1 == 1 and B & 1 == 0:
    n = (B-A)//2
    print(A^(n&1)^B)
else:
    n = (B-A+1)//2
    print(n&1)
