def check(l, s, p):
    for i in range(len(l)):
        l_i = l[i]
        cnt = 0
        for j in range(1,len(l_i)):
            cnt += s[l_i[j]-1]
        if cnt % 2 != p[i]:
            return False
    return True


n,m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]
p = list(map(int, input().split()))

ans = 0
for k in range(2**n):
    s = []
    for i in range(n):
        s.append( int(k & 1<<i == 1<<i) )
    ans += int(check(l,s,p))
print(ans)
