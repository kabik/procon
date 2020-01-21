def conb(a, b):
    nume = 1
    deno = 1
    for i in range(b):
        nume *= a - i
        deno *= i + 1

    return int(nume / deno)


n = int(input())

cnt_dict = {}
for i in range(n):
    si = input()
    si_sorted = ''.join( sorted(si) )
    if si_sorted in cnt_dict:
        cnt_dict[ si_sorted ] = cnt_dict[ si_sorted ] + 1
    else:
        cnt_dict[ si_sorted ] = 1

sum = 0
for k in cnt_dict:
    v = cnt_dict[k]
    if v > 1:
        sum += conb(v, 2)

print(sum)
