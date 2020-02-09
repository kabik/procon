n = int(input())
l = list(map(int, input().split()))
l.sort()

same = False
for i in range(0, n-1):
    if l[i] == l[i+1]:
        same = True
        break

print('NO' if same else 'YES')
