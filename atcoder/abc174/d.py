import sys
input = sys.stdin.readline

N = int(input())
C = input()

bad_w = 0
red = 0
ok = True
for i in range(N-1,-1,-1):
    if C[i] == 'R':
        red += 1
        ok = False
    if not ok and C[i] == 'W':
        bad_w += 1

good_red = 0
for i in range(red):
    if C[i] == 'R':
        good_red += 1


print( min(bad_w, N-bad_w, red-good_red) )
