N, K = map(int, input().split())

if K & 1:
    m = N//K
    print(m**3)
else:
    m = N//(K//2)
    print( ((m+1)//2)**3 + (m//2)**3 )
