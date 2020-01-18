h = int(input())
w = int(input())
n = int(input())

l = h if h > w else w
if n % l == 0:
    print(int(n/l))
else:
    print(int(n/l)+1)
