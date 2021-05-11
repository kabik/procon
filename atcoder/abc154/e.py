def f(k, n):
    n_str = str(n)
    digit = len(n_str)
    head = int(n_str[0])
    rest = int(n_str[1:]) if digit > 1 else 0

    if k == 1:
        return 9*(digit-1) + head
    if k == 2:
        if n <= 10:
            return 0
        else:
            return 9 * (digit-1) * (head-1) + f(1,rest) + f(2, 10**(digit-1)-1)
    if k == 3:
        if n < 111:
            return 0
        else:
            return 9**2 * (digit-1)*(digit-2)//2 * (head-1) + f(2,rest) + f(3, 10**(digit-1)-1)


n = int(input())
k = int(input())

print(f(k,n))
