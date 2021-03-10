from itertools import product
from collections import Counter

N = int(input())
patterns = []
for i in range(1,len(str(N))+1):
    patterns.extend(product('357', repeat=i))

ans = 0
for pat in patterns:
    num_str = ''.join(pat)
    num = int(num_str)
    ctr = Counter(str(num))
    if num <= N and '3' in ctr and '5' in ctr and '7' in ctr:
        ans += 1
print(ans)
