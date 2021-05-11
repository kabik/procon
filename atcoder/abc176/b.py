N = input()
sm = 0
for i in range(len(N)):
    sm += int(N[i])

if sm % 9 == 0:
    print('Yes')
else:
    print('No')
