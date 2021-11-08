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


N = int(random.randint(2, 5)) # 2 <= h <= 5
M = int(random.randint(1, 5))

UV_CAND = []
for i in range(1,N+1):
    for j in range(1,N+1):
        if i != j:
            UV_CAND.append([i,j])

UV = random.sample(UV_CAND, k=M)

print(N,M)
for uv in UV:
    print(*uv)
