X,Y,A,B = map(int, input().split())

ans = -1
while X < Y:
    if X * A < X + B:
        X *= A
        ans += 1
    else:
        if (Y-X) % B == 0:
            ans += (Y-X) // B
        else:
            ans += (Y-X) // B + 1
        X = Y
print(ans)
