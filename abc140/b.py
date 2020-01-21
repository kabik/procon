n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

sum = 0
for i in range(n):
    now = a[i] - 1
    pre = a[i-1] - 1
    sum += b[ now ]
    if i > 0 and now - 1 == pre:
        sum += c[ pre ]

print(sum)
