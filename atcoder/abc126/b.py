def is_month(t):
    return 1 <= int(t) <= 12

s = input()
pre, suf = s[:2], s[2:]

if is_month(pre) and is_month(suf):
    print('AMBIGUOUS')
elif not is_month(pre) and not is_month(suf):
    print('NA')
elif is_month(pre) and not is_month(suf):
    print('MMYY')
else:
    print('YYMM')
