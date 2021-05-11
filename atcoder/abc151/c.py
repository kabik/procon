n, m = map(int, input().split())
p = []
s = []

for i in range(0, m):
    pi, si = map(str, input().split())
    p.append( int(pi) )
    s.append( si )


done = []
for i in range(0,n):
    done.append(False)
wa_num = []
for i in range(0,n):
    wa_num.append(0)

ac = 0
for i in range(0, m):
    num = p[i] - 1
    if not done[num]:
        if s[i] == 'WA':
            wa_num[num] += 1
        else: # 'AC':
            ac += 1
            done[num] = True

wa = 0
for i in range(0,n):
    if done[i]:
        wa += wa_num[i]

print(ac, wa)
