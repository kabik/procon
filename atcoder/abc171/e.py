import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

sm = 0
for a in A:
    sm ^= a
for a in A:
    print(sm^a, end=' ')
print()
