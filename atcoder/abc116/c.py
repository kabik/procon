N = int(input())
H = list(map(int, input().split()))
H.append(0)

sm = sum(H)
ans = 0
while sm > 0:
    for i in range(N):
        if H[i] > 0:
            H[i] -= 1
            sm -= 1
            if H[i+1] == 0:
                ans += 1
print(ans)
