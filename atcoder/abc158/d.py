s = input()
N = int(input())
Q = [input().split() for _ in range(N)]

head = ''
tail = ''
reverse = 0

for q in Q:
    if int(q[0]) == 1:
        reverse = 1 - reverse
    elif int(q[1]) == 1:
        if reverse:
            tail += q[2]
        else:
            head += q[2]
    else:
        if reverse:
            head += q[2]
        else:
            tail += q[2]

if reverse:
    print(tail[::-1] + s[::-1] + head)
else:
    print(head[::-1] + s + tail)

"""
a
8
2 2 a
2 1 b
1
2 2 c
1
1
2 1 x
2 2 y
"""
