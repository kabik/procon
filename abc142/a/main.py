n = int(input())

if n == 1:
    print(1)
elif n % 2 == 1:
    print( (int(n/2) + 1) / n )
else:
    print( int(n/2) / n )
