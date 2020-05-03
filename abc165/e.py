N, M = map(int, input().split())

if M % 2 == 1:
    ll, lr, rl, rr = 1, M, M+1, M*2+1
    for i in range(M//2):
        print(ll+i, lr-i)
    for i in range(M//2+1):
        print(rl+i, rr-i)
else:
    ll, lr, rl, rr = 1, M+1, M+2, M*2+1
    for i in range(M//2):
        print(ll+i, lr-i)
        print(rl+i, rr-i)
