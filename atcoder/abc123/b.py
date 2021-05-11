import itertools

l = [int(input()) for _ in range(5)]
order_list = list(itertools.permutations(l))

min = 10**7
for order in order_list:
    sum = 0
    for i in range(4):
        sum += order[i]
        if sum % 10 > 0:
            sum += 10 - sum % 10
    sum += order[4]

    if sum < min:
        min = sum

print(min)
