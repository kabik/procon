import math


h,n = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]


eff_ind = 0
eff_max = 0
for i in range(len(ab)):
    rate = ab[i][0]/ab[i][1]
    if rate > eff_max:
        eff_max = rate
        eff_ind = i
    print(i, rate)

used = 0
while h >= ab[eff_ind][0]:
    h -= ab[eff_ind][0]
    used += ab[eff_ind][1]
    print('(h,used)=',h, used)



print(eff_ind)
print(h)
print(used)

if h > 0:
    min = 10**10
    min_ind = 0
    times = 0
    for i in range(len(ab)):
        a,b = ab[i][0], ab[i][1]
        n = math.ceil(h/a)
        if b*n < min:
            min = b*n
            min_ind = i
            times = n
    used += ab[min_ind][1] * times
    print('min_ind' , min_ind, 'times', times)

print(used)
