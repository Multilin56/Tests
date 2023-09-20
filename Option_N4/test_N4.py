x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

#gg

if ((x1+y1) % 2 != 0 and (x2+y2) % 2 != 0 or (x1+y1) % 2 == 0 and (x2+y2) % 2 == 0):
    x = x1 - x2
    y = y1 - y2
    while(True):
        a = (x1+x2) / 2
        if (y1 > y2):
            b = 1