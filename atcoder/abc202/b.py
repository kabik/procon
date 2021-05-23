S = input()
for i in range(len(S)):
    c = S[-1-i]
    r = c
    if c == '6':
        r = '9'
    elif c == '9':
        r = '6'
    print(r, end='')
print()
