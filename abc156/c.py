N = int(input())
X = list(map(int, input().split()))

mini = 10**10
for p in range(1, 101):
    used_hp = 0
    for x in X:
        used_hp += (x-p)**2
    mini = min(mini, used_hp)

print(mini)
