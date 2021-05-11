N = int(input())

divs = [1] * (N+1)

ans = 1
for i in range(2, N+1):
    if divs[i] == 1:  # prime
        k = i
        while k <= N:
            m = k
            cnt = 1
            while m % i == 0:
                cnt += 1
                m //= i
            divs[k] *= cnt
            k += i
        ans += i*2
    else:
        ans += i*divs[i]
print(ans)
