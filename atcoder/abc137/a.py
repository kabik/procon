a, b = map(int, input().split())

sum = a+b
sub = a-b
mul = a*b

if sum >= sub and sum >= mul:
    print(sum)
elif sub >= sum and sub >= mul:
    print(sub)
else:
    print(mul)
