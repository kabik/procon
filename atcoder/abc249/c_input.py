import random, string

def random_string(options: str, length: int) -> str:
    return ''.join(random.choices(options, k=length))

def random_string_lower(length: int) -> str:
    return random_string(options=string.ascii_lowercase, length=length)

def random_string_upper(length: int) -> str:
    return random_string(options=string.ascii_uppercase, length=length)

def random_string_letters(length: int) -> str:
    return random_string(options=string.ascii_letters, length=length)

def random_string_digits(length: int) -> str:
    return random_string(options=string.digits, length=length)

def random_string_mix(length: int) -> str:
    return random_string(options=string.ascii_letters + string.digits, length=length)


H = int(random.randint(2, 5)) # 2 <= h <= 5
W = int(random.randint(2, 5))
A = [[int(random.randint(1, 10)) for _ in range(W)] for _ in range(H)]
N = int(random.randint(1, 10))

print(H, W)
for a in A:
    print(*a)

print(N)

print(random_string('BW', N))
print(random_string_upper(N))
print(random_string_letters(N))
print(random_string_digits(N))
print(random_string_mix(N))
