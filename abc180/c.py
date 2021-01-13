N = int(input())

R = int(N**0.5)
l = []
for i in range(1, R+1):
    if N % i == 0:
        l.append(i)
        if i != N//i:
            l.append(N//i)
l.sort()
for k in l:
    print(k)
