S = input()

if len(S) == 1:
    if S.islower():
        print('Yes')
    else:
        print('No')
else:
    if S[0::2].islower() and S[1::2].isupper():
        print('Yes')
    else:
        print('No')
