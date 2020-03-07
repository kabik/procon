n, a, b = map(int, input().split())

k = n // (a+b)
l = n - (a+b) * k
l = a if l > a else l

ans = k * a + l
print(ans)
