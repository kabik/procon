n = int(input())
mset = set([x*y for x in range(1,10) for y in range(1,10)])
print('Yes') if n in mset else print('No')
