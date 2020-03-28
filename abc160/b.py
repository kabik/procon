X = int(input())

h = (X // 500) * 1000
h += ((X % 500) // 5) * 5

print(h)
