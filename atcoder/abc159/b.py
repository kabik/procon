s = input()

def is_kaibun(str):
    for i in range( len(str)//2 ):
        if str[i] != str[-i-1]:
            return False
    return True

n = len(s)
if is_kaibun(s) and is_kaibun(s[:(n-1)//2]) and is_kaibun(s[(n+3)//2-1:]):
    print('Yes')
else:
    print('No')
