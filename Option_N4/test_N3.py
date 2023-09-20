import math

n = int(input())

#gg

arr = []
a1 = 0
a2 = (int(input()))
a3 = 1
answer = 0
for i in range(n-1):
    a1 = (int(input()))
    if (a1 == a2):
        a3 += 1
    else:
        answer += math.floor(a3/3)
        a2 = a1
        a3 = 1

    # print(a1)
    # print(a2)
    # print(a3)
    # print(answer)

if (a3 >= 3):
    answer += math.floor(a3 / 3)

print(answer)