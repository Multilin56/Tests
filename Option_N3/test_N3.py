import math

n = int(input())
a = int(input())
b = int(input())

#gg

c = 0
for i in range(n):
    if ((i+1) % b == 0 and (i+1) % a == 0):
        c += 1

print(math.floor(n/a) + math.floor(n/b) - c)