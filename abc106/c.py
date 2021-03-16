S = input()
K = int(input())
M = 5 * 10**15

cnt = 0
for c in S:
    if c == '1':
        cnt += 1
        if cnt == K:
            print(1)
            break
    else:
        print(c)
        break
