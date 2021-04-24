A,B,K = map(int, input().split())
ans = []
for i in range(K):
    a = A+i
    if A <= a <= B:
        ans.append(a)
    b = B-K+1+i
    if A <= b <= B:
        ans.append(b)
ans = sorted(list(set(ans)))
for a in ans:
    print(a)
