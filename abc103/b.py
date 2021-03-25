S = input()
T = input()

ans = 'No'
for i in range(len(S)):
    if S[i+1:] + S[:i+1] == T:
        ans = 'Yes'
        break
print(ans)
