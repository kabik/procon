import sys
def debug(**kwargs): print(f'DEBUG: {kwargs}', file=sys.stderr)

W = int(input())
A = set()
for i in range(1,101):
    A.add(i)
    A.add(100*i)
    A.add(10000*i)

print(len(A))
print(*A)
