N = int(input())

checked = {}
cnt = 0
i = 2
while i*i <= N:
    if i not in checked:
        k = i*i
        while k <= N:
            checked[k] = True
            k *= i
            cnt += 1
    i+=1
print(N-cnt)
