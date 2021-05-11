n, k = map(int, input().split())
h = list(map(int, input().split()))

l = [i for i in h if i >= k]
print(len(l))
