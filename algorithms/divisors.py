def divisors(n):
    l = []
    for i in range(1, int(n**0.5) +1):
        if n % i == 0:
            l.append(i)
            if n // i != i:
                l.append(n//i)
    return sorted(l)


if __name__ == "__main__":
    # test divisors()
    print('-- test primes() --')
    print(36, divisors(36))
    print(100, divisors(100))
