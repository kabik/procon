N = int(input())
A = list(map(int, input().split()))

pos = 0
mx = pos
diff = 0
diff_mx = 0
for a in A:
    diff_mx = max(diff_mx, diff+a)
    mx = max(mx, pos + diff_mx)

    diff += a
    pos += diff
print(mx)
