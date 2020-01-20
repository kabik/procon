n = int(input())
a = list(map(int, input().split()))

denomi = 0
for ai in a:
    denomi += 1/ai

print(1 / denomi)
