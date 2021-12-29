import sys

def debug(**kwargs): print(f'DEBUG: {kwargs}', file=sys.stderr)

N = int(input())

ans = 0
pre_y = -1
root = int(N**0.5)
for x in range(1,root+1):
    y = N//x
    ans += y + (pre_y-y)*(x-1)
    #debug(x=x, y=y, plus=(pre_y-y)*(x-1), pre_y=pre_y, ans=ans)
    pre_y = y
if N//root != root:
    #debug(root=root)
    ans += root*(N//root-root)
print(ans)
