A,B,C = map(int, input().split())
K = int(input())
m = max(A,B,C)
if m == A:
    print(A*2**K + B + C)
elif m == B:
    print(A + B*2**K + C)
else:
    print(A + B + C*2**K)
