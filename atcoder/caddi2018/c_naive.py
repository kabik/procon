def LI(): return list(map(int, input().split()))
N,P = LI()

for x in range(max(1, P//N), 0, -1):
    if x**N <= P and P%(x**N) == 0:
        print(x)
        break
