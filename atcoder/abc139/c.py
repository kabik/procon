n = int(input())
h = list(map(int, input().split()))

step_max = 0
r_step = 0
for i in reversed(range(n-1)):
    if h[i] >= h[i+1]:
        r_step += 1
    else:
        r_step = 0

    if r_step > step_max:
        step_max = r_step

print(step_max)
