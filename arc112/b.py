B,C = map(int, input().split())

if B > 0:
    if C == 1:
        print(2)
    elif C >= 2*B:
        print((C-1)//2 + 2*B + (C-2)//2 + 1)
    else:
        print((C-1)//2 + C + (C-2)//2 + 1)
elif B == 0:
    if C < 2:
        print(1)
    else:
        print(C)
else: # B < 0:
    if C >= -2*B:
        print(C//2 + (C-1)//2 + 1 -B*2)
    else:
        print(C//2 + (C-1)//2 + 1 + C)
