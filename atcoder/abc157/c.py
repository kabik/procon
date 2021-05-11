N,M = map(int, input().split())
SC = [list(input().split()) for _ in range(M)]

ans = -1
if N==1:
    for i in range(0,10):
        i_str = str(i)
        pass_cond = True
        for sc in SC:
            s = int(sc[0])
            c = sc[1]

            if s > len(i_str) or i_str[ s-1 ] != c:
                pass_cond = False

        if pass_cond:
            ans  = i
            break
else:
    for i in range(10**(N-1), 10**N):
        i_str = str(i)
        pass_cond = True
        for sc in SC:
            s = int(sc[0])
            c = sc[1]

            if s > len(i_str) or i_str[ s-1 ] != c:
                pass_cond = False

        if pass_cond:
            ans  = i
            break


print(ans)
