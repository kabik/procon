n = input()
ans = ''
for c in n:
    if c == '1':
        ans += '9'
    elif c == '9':
        ans += '1'
    else:
        ans += c
print(ans)
