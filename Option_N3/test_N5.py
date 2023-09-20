import math

n = int(input())

#gg

s = 0
while(n != 0):
    s += 1
    print(n)
    if (n % 2 == 0):
        n = n/2
    else:
        n -= 1

print(s)