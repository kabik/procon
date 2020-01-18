s = input()

result = 'Yes'
for i in range(len(s)):
    if i % 2 == 0 and s[i] == 'L': # odd
        result = 'No'
    elif i % 2 == 1 and s[i] == 'R': # even
        result = 'No'

print(result)
