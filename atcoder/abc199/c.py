N = int(input())
S = list(input())
Q = int(input())
TAB = [list(map(int, input().split())) for _ in range(Q)]

V = [ S[:N], S[N:] ]
flip = 0
for t,a,b in TAB:
    if t == 1:
        a -= 1
        b -= 1
        if a < N:
            tmp = V[flip][a]
            if b < N:
                V[flip][a] = V[flip][b]
                V[flip][b] = tmp
            else:
                V[flip][a] = V[1-flip][b-N]
                V[1-flip][b-N] = tmp
        else:
            tmp = V[1-flip][a-N]
            if b < N:
                V[1-flip][a-N] = V[flip][b]
                V[flip][b] = tmp
            else:
                V[1-flip][a-N] = V[1-flip][b-N]
                V[1-flip][b-N] = tmp
    else:
        flip = 1 - flip
print(''.join(V[flip]+V[1-flip]))
