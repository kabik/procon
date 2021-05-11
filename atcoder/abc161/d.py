d = {
        0: [0, 1],
        1: [0, 1, 2],
        2: [1, 2, 3],
        3: [2, 3, 4],
        4: [3, 4, 5],
        5: [4, 5, 6],
        6: [5, 6, 7],
        7: [6, 7, 8],
        8: [7, 8, 9],
        9: [8, 9]
    }

def next_list(m):
    tail = int(str(m)[-1])
    return d[tail]

def lunlun(k):
    if k < 10:
        return k

    ans = [-1, [1,2,3,4,5,6,7,8,9]]
    cnt = 9
    for i in range(2,11):
        ans.append([])
        for pre in ans[i-1]:
            for n in next_list(pre):
                next = int( str(pre)+str(n) )
                ans[i].append(next)
                cnt += 1
                if cnt == K:
                    return next

K = int(input())
print(lunlun(K))
