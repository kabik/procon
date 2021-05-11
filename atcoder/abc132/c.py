n = int(input())
d = sorted(list(map(int, input().split())))

mid_l = len(d)//2 - 1
mid_r = mid_l + 1
print(d[mid_r] - d[mid_l])
