import sys
input = sys.stdin.readline

X, Y, A, B, C = map(int, input().split())
P = sorted(list(map(int, input().split())), reverse=True)
Q = sorted(list(map(int, input().split())), reverse=True)
R = sorted(list(map(int, input().split())), reverse=True)

ans = sum(P[:X]) + sum(Q[:Y])
x = X-1
y = Y-1
for z in range(C):
    if x < 0:
        if R[z] > Q[y]:
            ans += R[z] - Q[y]
            y -= 1
    elif y < 0:
        if R[z] > P[x]:
            ans += R[z] - P[x]
            x -= 1
    else:
        if R[z] > P[x] >= Q[y]:
            ans += R[z] - Q[y]
            y -= 1
        elif R[z] > Q[y] > P[x]:
            ans += R[z] - P[x]
            x -= 1
        elif P[x] >= R[z] > Q[y]:
            ans += R[z] - Q[y]
            y -= 1
        elif Q[y] >= R[z] > P[x]:
            ans += R[z] - P[x]
            x -= 1
print(ans)
