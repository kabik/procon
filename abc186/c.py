N = int(input())

def lucky(n, k):
    while n > 0:
        if n % k == 7:
            return True
        n //= k
    return False

ans = 0
for i in range(1, N+1):
    if not lucky(i, 10) and not lucky(i, 8):
        ans += 1
print(ans)
