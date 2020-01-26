nums = {1:1}
def num(k):
    if k in nums:
        return nums[k]
    else:
        nums[k] = 2 * num(k//2) + 1
        return nums[k]

h = int(input())
print(num(h))
