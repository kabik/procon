N = int(input())
A = list(map(int, input().split()))

def cmb2(n):
    return n * (n-1) // 2

nums = {}
for a in A:
    if a in nums:
        nums[a] += 1
    else:
        nums[a] = 1

sum = 0
for key in nums:
    num = nums[key]
    sum += cmb2(num)

for k in range(N):
    ans = sum - cmb2( nums[A[k]] ) + cmb2( nums[A[k]]-1 )
    print(ans)
