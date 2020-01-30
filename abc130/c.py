w,h,x,y = map(int, input().split())

side = (x == 0 or x == w or y == 0 or y == h \
    or y/x == h/w or y == -h/w * x + h \
    or x != w/2 or y != h/2) \
    and not (x == w/2 and y == h/2)
area = w * h

print(area/2, int(not side))
