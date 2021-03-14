A,B,W = map(int, input().split())


m,M = 10**9, -1
for i in range(1,1000*W+1):
    if A*i <= 1000*W <= B*i:
        m = min(m, i)
        M = max(M, i)
if m == 10**9:
    print('UNSATISFIABLE')
else:
    print(m, M)
