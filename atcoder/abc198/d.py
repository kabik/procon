import sys
from collections import Counter
from itertools import permutations

input = sys.stdin.buffer.readline
def SI(): return [c for c in input().rstrip().decode()]
def LLSI(rows_number): return [SI() for _ in range(rows_number)]

S = LLSI(3)

s_set = list(set(S[0]+S[1]+S[2]))
if len(s_set) > 10:
    print('UNSOLVABLE')
else:
    for pat in permutations(map(str, range(0, 10)), len(s_set)):
        d = dict()
        for i in range(len(s_set)):
            d[s_set[i]] = pat[i]
        if d[S[0][0]] == '0' or d[S[1][0]] == '0' or d[S[2][0]] == '0':
            continue
        n1 = ''.join( [d[c] for c in S[0]] )
        n2 = ''.join( [d[c] for c in S[1]] )
        n3 = ''.join( [d[c] for c in S[2]] )
        if int(n1) + int(n2) == int(n3):
            print(n1)
            print(n2)
            print(n3)
            break
    else:
        print('UNSOLVABLE')
