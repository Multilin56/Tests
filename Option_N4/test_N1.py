import math

n = int(input())
d = int(input())

#gg

if (d == 1):
    print(math.floor(n/7))
else:
    print(math.floor((n-(7-d))/7))