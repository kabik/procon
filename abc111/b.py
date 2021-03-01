N = int(input())
for i in range(10):
    if i*111 < N <= (i+1)*111:
        print((i+1)*111)
        break
