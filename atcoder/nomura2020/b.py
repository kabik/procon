T = input()

l = []
for i in range(len(T)):
    if T[i] == 'P':
        l.append('P')
    else:
        l.append('D')
ans = ''.join(l)
print(ans)
