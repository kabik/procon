X = int(input())

running = True
for a in range(-1000, 1001):
    if not running:
        break
    for b in range(-1000, 1001):
        if a**5 - b**5 == X:
            print(a, b)
            running = False
            break
