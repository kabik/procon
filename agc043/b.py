N = int(input())
S = input()

def intlist(s):
    l = []
    for c in s:
        l.append(int(c))
    return l

def cut(list):
    l = [list[0]]
    if len(list) > 1:
        l.append(list[1])
    compressed = False
    for i in range(2, len(list)):
        if list[i] != list[i-1] or list[i] != list[i-2]:
            l.append(list[i])
        else:
            compressed = True
    if len(l) == 1 and compressed:
        l.append( l[0] )
    return l

X = intlist(S)
while len(X) > 1:
    next = []
    for i in range(len(X)-1):
        v = abs(X[i] - X[i+1])
        next.append(v)
    X = cut(next)

if len(next) > 0:
    print(next[0])
else:
    print(0)
