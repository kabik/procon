n = int(input())
h = list(map(int, input().split()))

result = 'Yes'
h[0] -= 1
for i in range(1,n):
    if h[i-1] < h[i]:
        h[i] -= 1
    elif h[i-1] > h[i]:
        result = 'No'
        break

print(result)
