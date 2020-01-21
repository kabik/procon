n = int(input())

done_list = []
cnt = 0
for i in range(1, n+1):
    s = str(i)
    l = len(s)
    head = s[0]
    tail = s[l - 1]

    if l > 1 and head == tail:
        cnt += 1
        #print(i, i, cnt)
        continue
    if i in done_list: continue
    if tail == '0': continue

    if l == 1:
        cnt += 1
        #print(i, i, cnt)
        k = int(head+head)
        if k <= n:
            done_list.append(k)
            cnt += 2
            #print(i, k, cnt)

    if l == 2:
        k = int(tail+head)
        if k <= n:
            if i == k:
                cnt += 1
                #print(i, k, cnt)
            else:
                done_list.append(k)
                cnt += 2
                #print(i, k, cnt)

    for mid in range( pow(10, l) ):
        k = int(tail + str(mid) + head)
        #print(i, mid, k)
        if k > n: break
        if not k in done_list:
            done_list.append(k)
            cnt += 2

print(cnt)
