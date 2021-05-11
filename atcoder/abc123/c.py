N = int(input())
L = []
for _ in range(5):
    L.append(int(input()))

mn = min(L)
ans = (-(-N//mn)) + 4
print(ans)
