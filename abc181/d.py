from collections import Counter

S = input()
cnt = Counter(S)

ans = 'No'
if len(S) == 1:
    if S == '8':
        ans = 'Yes'
elif len(S) == 2:
    if int(S) % 8 == 0:
        ans = 'Yes'
    elif int(S[::-1]) % 8 == 0:
        ans = 'Yes'
else:
    for i in range(112, 1000, 8):
        if not Counter(str(i))-cnt:
            ans = 'Yes'
            break
print(ans)
